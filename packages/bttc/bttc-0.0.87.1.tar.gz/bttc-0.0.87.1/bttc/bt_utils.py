# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utility to support common BT operations/methods."""
import datetime
from functools import partial
import logging
import time

from mobly import signals
from mobly.controllers import android_device
import bttc
from bttc import bt_data
from bttc import common_data
from bttc import constants
from bttc import core
from bttc import errors
from bttc import utils
from bttc.utils import device_factory
from bttc.utils import logcat
from bttc.utils import log_parser
from bttc.utils import retry

import re
from typing import Any, Sequence, TypeAlias, Union


BINDING_KEYWORD = 'bt'
AUTO_LOAD = True
ANDROID_DEVICE: TypeAlias = android_device.AndroidDevice
BT_ADAPTER_STATE: TypeAlias = constants.BluetoothAdapterState
BT_BONDED_STATE: TypeAlias = constants.BluetoothBondedState
BT_PAIRED_DEVICE: TypeAlias = bt_data.PairedDeviceInfo
BT_BONDED_DEVICE: TypeAlias = bt_data.BondedDeviceInfo

# Logcat message timestamp format
_DATETIME_FMT = constants.LOGCAT_DATETIME_FMT

# Pattern to match message of logcat service.
_LOGCAT_MSG_PATTERN = constants.LOGTCAT_MSG_PATTERN


class BTModule(core.UtilBase):
  """BT module to hold BT related functions define in this module."""

  NAME = BINDING_KEYWORD
  DESCRIPTION = (
      'Utility to support Bluetooth base operations such as turn on/off '
      'Bluetooth.')

  def __init__(self, ad: ANDROID_DEVICE):
    super().__init__(ad)
    self._bind(crash_since)
    self._bind(dump_bluetooth_manager)
    self._bind(enable_snoop_log)
    self._bind(enable_gd_log_verbose)
    self._bind(enable_log_verbose)
    self._bind(get_bluetooth_mac_address)
    self._bind(get_bonded_devices)
    self._bind(get_device_mac_by_name)
    self._bind(get_connected_ble_devices)
    self._bind(get_current_le_audio_active_group_id)
    self._bind(get_name)
    self._bind(is_le_audio_device_connected)
    self._bind(is_bluetooth_enabled, 'is_enabled')
    self._bind(list_paired_devices)
    self._bind(set_fast_pair_halfsheet)
    self._bind(set_name)
    self._bind(unbond_device)
    self.shell = bttc.safe_adb_shell(ad)
    self.enable = partial(toggle_bluetooth, ad=ad, enabled=True)
    self.disable = partial(toggle_bluetooth, ad=ad, enabled=False)

  @property
  def enabled(self):
    return self.is_enabled()

  @property
  def bonded_devices(self):
    return {device.name: device for device in self.get_bonded_devices()}

  @property
  def bonded_device_names(self):
    return [device.name for device in self.bonded_devices]

  @property
  def le_state(self) -> BT_ADAPTER_STATE:
    return constants.BluetoothAdapterState.from_int(
        self.ad.sl4a.bluetoothGetLeState())

  @property
  def mac_address(self) -> str:
    return self.get_bluetooth_mac_address()

  @property
  def name(self) -> str:
    return self.get_name()

  @property
  def paired_devices(self):
    return {
        d.name: d
        for d in self.list_paired_devices(only_name=False)}

  @property
  def paired_device_names(self):
    return self.list_paired_devices()

  def disable_fastpair(self):
    """Disables Fastpair feature."""
    self.set_fast_pair_halfsheet(False)

  def disconnect(
      self,
      mac_address: str,
      timeout_sec: float = 30):
    """Disconnects the BT device with given MAC address.

    TODO: Add unit test case(s)

    Args:
      mac_address: The Bluetooth mac address of the peripheral device.
      timeout: Number of seconds to wait for the devices to disconnect the
        peripheral device.
    """
    if not self.is_connect_with(mac_address):
      self.ad.log.info('Device %s is not connected yet.', mac_address)
      return

    self.ad.sl4a.bluetoothDisconnectConnected(mac_address)
    self.wait_disconnect(
        mac_address=mac_address, timeout_sec=timeout_sec)

  def enable_fastpair(self):
    """Enables Fastpair feature."""
    self.set_fast_pair_halfsheet(True)

  def factory_reset(self):
    """Factory resets the Bluetooth.

    Raises:
      errors.BluetoothAdapterError: Under unexpected Bluetooth adapter state.
    """
    self.ad.log.info('Performing a factory reset on Bluetooth...')
    self.enable()
    self.wait_state(enabled=True)
    for _, device_info in self.bonded_devices.items():
      self.unbond_device(device_info.mac_addr)

    # Buffer time between unbonding and factory resetting.
    time.sleep(5)
    self.ad.sl4a.bluetoothFactoryReset()
    bt_adapter_on_state = constants.BluetoothAdapterState.STATE_ON
    if not self.wait_adapter_state(states=bt_adapter_on_state):
      raise errors.BluetoothAdapterError(
          self.ad,
          f'Bluetooth Adapter is not "{bt_adapter_on_state.name}". '
          f'current state: {self.le_state.name}')
    self.wait_state(enabled=True)

  def is_connect_with(self, name_or_mac_addr: str) -> bool:
    """Checks if the given BT name or mac address is connected.

    TODO: Add unit test case(s)
    """
    connected_info_list = [
        {bonded_device.name, bonded_device.mac_addr}
        for _, bonded_device in self.bonded_devices.items()
        if bonded_device.is_connected()
    ]
    for connected_info in connected_info_list:
      if name_or_mac_addr in connected_info:
        return True

    return False

  def pair(
      self,
      mac_address: str,
      attempts: int = 3,
      enable_pairing_retry: bool = True):
    """Pairs the peripheral Bluetooth device by its MAC address.

    If the devices are already connected, does nothing. If
    the devices are paired but not connected, connects the devices. If the
    devices are neither paired nor connected, this method pairs and connects the
    devices.

    TODO: Add unit test case(s)

    Args:
      mac_address: The Bluetooth mac address of the peripheral device.
      attempts: Number of attempts to discover and pair the peripheral device.
      enable_pairing_retry: Bool to control whether the retry mechanism is used
        on bonding failure, it's enabled if True.
    """
    if self.is_connect_with(mac_address):
      self.ad.log.info('Device %s already paired and connected', mac_address)
      return

    bonded_device_mac_addr_set = {
        bonded_device.mac_addr
        for _, bonded_device in self.bonded_devices.items()}

    if mac_address in bonded_device_mac_addr_set:
      self.ad.log.info(
          'Connecting bonded device with MAC address=%s...', mac_address)
      self.ad.sl4a.bluetoothConnectBonded(mac_address)
      self.wait_connection(mac_address)
      return

    self.ad.log.info('Initiating pairing to the device "%s"...', mac_address)
    self.ad.sl4a.bluetoothStartPairingHelper()
    for i in range(attempts):
      self.ad.sl4a.bluetoothDiscoverAndBond(mac_address)
      try:
        self.wait_connection(mac_address)
        return
      except Exception as ex:
        if i + 1 < attempts and enable_pairing_retry:
          self.ad.log.warning(
              'Failed to connect the device "%s" on Attempt %d. '
              'Retrying pairing...', mac_address, i + 1)
          continue

        raise ex

  def restart(self):
    """Restarts the Bluetooth.

    This method will disable and then enable the Bluetooth to restart it.
    """
    self.disable()
    self.enable()

  def wait_adapter_state(
      self,
      states: BT_ADAPTER_STATE | set[BT_ADAPTER_STATE],
      timeout_sec: int = 30,
      exception: Exception | signals.TestError | None = None) -> bool:
    """Waits for expected BT adapter state.

    Args:
      state: Expected BT adapter state.
      timeout_sec: Time to wait the desired BT adapter state.

    Returns:
      True if the desire state is obtained.
    """
    def wait_func(bt):
      return bt.le_state

    expected_states = states if isinstance(states, set) else {states}

    def expected_func(state):
      return state in expected_states

    return utils.wait_until(
        timeout_sec=timeout_sec,
        condition_func=wait_func,
        func_args=[self],
        expected_func=expected_func,
        exception=exception)

  def wait_connection(
      self,
      mac_address: str,
      timeout_sec: float = 30,
      wait_time_sec: float = 0.5) -> float:
    """Waits for connection of BT with given MAC address.

    TODO: Add unit test case(s)

    Returns:
      The connection time in seconds.

    Raises:
      errors.BluetoothConnectError: Failed to wait for success of connection.
    """
    device_start_time = self.ad.gm.device_time
    start_time = time.time()
    end_time = start_time + timeout_sec
    while time.time() < end_time:
      if self.is_connect_with(mac_address):
        return time.time() - start_time

      time.sleep(wait_time_sec)

    reason = logcat.get_connection_fail_reason(self.ad, device_start_time)
    raise errors.BluetoothConnectError(
        f'Failed to connect device "{mac_address}" '
        f'within {timeout_sec} seconds.'
        f' Reason:{reason}')

  def wait_disconnect(
      self,
      mac_address: str,
      timeout_sec: float = 30,
      wait_time_sec: float = 0.5) -> float:
    """Waits for disconnection of BT with given MAC address.

    TODO: Add unit test case(s)

    Returns:
      The time in seconds in waiting.
    """
    start_time = time.time()
    end_time = start_time + timeout_sec
    while time.time() < end_time:
      if not self.is_connect_with(mac_address):
        return time.time() - start_time

      time.sleep(wait_time_sec)

    raise errors.BluetoothDisconnectError(
        f'Failed to disconnect device "{mac_address}" '
        f'within {timeout_sec} seconds.')

  def wait_state(
      self,
      enabled: bool = True,
      timeout_sec: float = 30) -> bool:
    """Waits for Bluetooth to be in the expected state.

    Args:
      enabled: True if Bluetooth status is enabled as expected.
      timeout_sec: Number of seconds to wait for Bluetooth to be in the expected
        state.

    Returns:
      True if the desire state is obtained.
    """
    return utils.wait_until(
        timeout_sec=timeout_sec,
        condition_func=self.is_enabled,
        func_args=[],
        expected_value=enabled,
        exception=signals.TestError(
            'Bluetooth is not %s within %d seconds on the device "%s".' %
            ('enabled' if enabled else 'disabled', timeout_sec,
             self.ad.serial)))


def bind(
    ad: Union[ANDROID_DEVICE, str],
    init_mbs: bool = False,
    init_sl4a: bool = False,
    init_snippet_uiautomator: bool = False,
    init_tl4a: bool = False) -> ANDROID_DEVICE:
  """Binds the input device with functions defined in module `bt_utils`.

  Sample Usage:
  ```python
  >>> from bttc import bt_utils
  >>> ad = bt_utils.bind('35121FDJG0005P', init_mbs=True, init_sl4a=True)
  >>> ad.bt.is_bluetooth_enabled()
  True
  >>> ad.bt.list_paired_devices()
  ['Galaxy Buds2 Pro', 'Galaxy Buds2 Pro']
  ```

  Args:
    ad: If string is given, it stands for serial of device. Otherwise, it should
        be the Android device object.
    init_mbs: True to initialize the MBS service of given device.
    init_sl4a: True to initialize the SL4A service of given device.

  Returns:
    The device with binded functions defined in `bt_utils`.
  """
  device = device_factory.get(
      ad, init_mbs=init_mbs,
      init_sl4a=init_sl4a,
      init_snippet_uiautomator=init_snippet_uiautomator,
      init_tl4a=init_tl4a)
  device.load_config({BINDING_KEYWORD: BTModule(device)})

  return device


def crash_since(
    device: android_device.AndroidDevice,
    start_time: str | None = None) -> common_data.CrashInfo:
  """Collects crash timestamp.

  Usage example:
  ```python
  >>> import bttc
  >>> dut = bttc.get('36121FDJG000GR')
  >>> device_time = dut.gm.device_time
  >>> dut.bt.crash_since(device_time)  # We actually have two crash occurred before `device_time`  # noqa: E501
  CrashInfo(total_num_crash=2, collected_crash_times=[])
  >>> dut.bt.crash_since()  # Collect all crash time
  CrashInfo(total_num_crash=2, collected_crash_times=['02-07 08:55:35.085', '02-07 09:08:12.584'])
  >>> dut.bt.crash_since('02-07 08:56:35.085')  # Collect crash timestamp after  '02-07 08:56:35.085'
  CrashInfo(total_num_crash=2, collected_crash_times=['02-07 09:08:12.584'])
  ```

  Args:
    device: Adb like device.
    start_time: start time in string format of `_DATETIME_FMT`. If not give, all
      crash timestamp will be collected.

  Returns:
    Crash information including total crash count and collected crash timestamp.
  """
  start_datetime_obj = None
  try:
    if start_time:
      start_datetime_obj = datetime.datetime.strptime(start_time, _DATETIME_FMT)
  except ValueError as ex:
    logging.error('Invalid time format = "%s"!', start_time)
    raise ex

  crash_time_info = common_data.CrashInfo()
  bluetooth_crash_header_pattern = re.compile(
      r'Bluetooth crashed (?P<num_crash>\d+) time')

  # The interested parsing content will look lik:
  # usky:/ # dumpsys bluetooth_manager | grep -A 20 "Bluetooth crashed"
  # Bluetooth crashed 2 time
  # 02-07 08:55:35.085
  # 02-07 10:35:04.011
  #
  bt_manager_messages = dump_bluetooth_manager(device).split('\n')
  for i, line in enumerate(bt_manager_messages):
    matcher = bluetooth_crash_header_pattern.match(line)
    if matcher:
      crash_num = int(matcher.group('num_crash'))
      logging.info('Total %s crash being detected!', crash_num)
      crash_time_info.total_num_crash = crash_num
      for line_num in range(i+1, len(bt_manager_messages)):
        crash_time = bt_manager_messages[line_num].strip()
        if not crash_time:
          break

        crash_datetime_obj = datetime.datetime.strptime(
            crash_time, _DATETIME_FMT)
        if (
            not start_datetime_obj or
            crash_datetime_obj >= start_datetime_obj):
          crash_time_info.collected_crash_times.append(crash_time)

    if crash_time_info.total_num_crash >= 0:
      break

  return crash_time_info


@retry.logged_retry_on_exception(
    retry_value=UnicodeDecodeError,
    retry_intervals=retry.FuzzedExponentialIntervals(
          initial_delay_sec=1,
          num_retries=5,
          factor=1.1))
def dump_bluetooth_manager(ad: android_device.AndroidDevice,
                           args: Sequence[str] = ()) -> str:
  """Dumps Bluetooth Manager log for the device.

  Args:
    args: Other arguments to be used in the dump command.

  Returns:
    Output of the dump command.
  """
  return ad.adb.shell(
      ('dumpsys', 'bluetooth_manager', *args)).decode()


def enable_snoop_log(ad: android_device.AndroidDevice) -> bool:
  """Enables Snoop log."""
  property_name = 'persist.bluetooth.btsnooplogmode'
  ad.log.info('Enabling Bluetooth Snoop log...')
  ad.adb.shell(f'setprop {property_name} full')
  property_setting = ad.adb.shell(
      f'getprop {property_name}').decode().strip()
  if property_setting == 'full':
    ad.log.info('Successfully enabled Bluetooth Snoop Log.')
    return True

  ad.log.warning(
      'Failed to enable Bluetooth Snoop Log with '
      'unexpected current setting="%s"', property_setting)
  return False


def enable_gd_log_verbose(ad: android_device.AndroidDevice) -> bool:
  """Enables bluetooth Gabeldorsche verbose log."""
  if int(ad.build_info['build_version_sdk']) >= 33:
    ad.log.info('Enabling Bluetooth GD verbose logging...')
    ad.adb.shell('device_config set_sync_disabled_for_tests persistent')
    ad.adb.shell('device_config put bluetooth '
                 'INIT_logging_debug_enabled_for_all true')
    out = ad.adb.shell(
        'device_config get bluetooth '
        'INIT_logging_debug_enabled_for_all').decode()
    if 'true' in out:
      ad.log.info('Successfully enabled Bluetooth GD verbose logging.')
      return True
  else:
    ad.log.warning(
        'Not TM or above build. Skip the enable GD verbose logging.')

  return False


def enable_log_verbose(ad: android_device.AndroidDevice):
  """Enables Bluetooth verbose logging."""
  ad.gm.props['log.tag.bluetooth'] = 'VERBOSE'
  ad.bt.disable()
  ad.bt.enable()


def get_bluetooth_mac_address(ad: android_device.AndroidDevice) -> str:
    """Gets Bluetooth mac address of an AndroidDevice."""
    ad.log.info('Getting Bluetooth mac address.')
    mac_address = ad.adb.shell(
            'settings get secure bluetooth_address').decode('utf8').strip()
    ad.log.info('Bluetooth mac address: %s', mac_address)
    return mac_address


def get_bonded_devices(
    ad: android_device.AndroidDevice) -> list[BT_BONDED_DEVICE]:
  """Retrieves information about bonded Bluetooth devices.

  Args:
    ad: The Android device object.

  Returns:
    A list of bonded device information objects.
  """
  return log_parser.parse_bonded_device_info(
      dump_bluetooth_manager(ad))


def get_connected_ble_devices(
    ad: android_device.AndroidDevice) -> list[dict[str, Any]]:
  """Returns devices connected through bluetooth LE.

  Returns:
       List of conncted le devices info.
  """
  return ad.sl4a.bluetoothGetConnectedLeDevices(
      constants.BluetoothProfile.GATT)


def get_current_le_audio_active_group_id(
    ad: android_device.AndroidDevice) -> int:
    """Gets current LE Audio active group ID.

    Returns:
      LE Audio group ID.
    """
    dump = dump_bluetooth_manager(
        ad, ('|', 'grep', '"currentlyActiveGroupId"', '||', 'echo', ' '))
    result = re.search(r'currentlyActiveGroupId: (.*)', dump)
    if result and result.group(1) != '-1':
      return int(result.group(1))
    ad.log.info('No LE Audio group active.')
    return -1


def get_device_mac_by_name(
    ad: android_device.AndroidDevice, bt_name: str) -> list[str]:
  """Retrieves the MAC address(es) of a paired Bluetooth device by its name.

  Args:
    ad: The Android device object.
    bt_name: The name of the Bluetooth device.

  Returns:
    A list of MAC addresses associated with the given device name.
    The list might contain multiple addresses if the device supports
    multiple Bluetooth profiles.

  Raises:
    Exception: If no paired device is found with the specified name.
  """

  paired_devices = ad.mbs.btGetPairedDevices()
  mac_address_list = []

  for device_info in paired_devices:
    if device_info['Name'] == bt_name:
      mac_address_list.append(device_info['Address'])

  if not mac_address_list:
    raise Exception(f'BT name={bt_name} does not exist!')

  return mac_address_list


def get_name(ad: android_device.AndroidDevice) -> str:
  """Retrieves the (Bluetooth) name of device.

  To use this function, the device need to support MBS (Mobly bundled snippets).

  Args:
    ad: The Android device object.

  Returns:
    Name of (Bluetooth) device.
  """
  return ad.bt.dump_bluetooth_manager((
      '|', 'grep', '-A5', '"Bluetooth Status"',
      '|', 'grep', 'name:')).strip().split(':')[1].strip()


def is_bluetooth_enabled(ad: android_device.AndroidDevice) -> bool:
  """Checks if Bluetooth is enabled on an Android device.

  Args:
    ad: The Android device object.

  Returns:
    True if Bluetooth is enabled, False otherwise.
  """
  return 'enabled: true' in dump_bluetooth_manager(
      ad, ('|', 'grep', '-A1', '"Bluetooth Status"', '||', 'echo', ' '))


def is_le_audio_device_connected(
    ad: android_device.AndroidDevice, mac_address: str) -> bool:
  """Checks if the LE Audio device is connected.

  Args:
    mac_address: Bluetooth MAC address of the LE Audio device.

  Returns:
    True iff the LE Audio device is connected.
  """
  # NOMUTANTS -- Grep keyword in dump.
  dump = dump_bluetooth_manager(ad, (
      '|', 'grep', '-B5',
      f'"group lead: XX:XX:XX:XX:{mac_address[-5:].upper()}"', '||', 'echo',
      ' '))
  return 'isConnected: true' in dump


def list_paired_devices(
    ad: android_device.AndroidDevice,
    only_name: bool = True) -> list[BT_PAIRED_DEVICE]:
  """Retrieves information about paired Bluetooth devices.

  Args:
    ad: The Android device object.
    only_name: If True, returns a list of paired device names only.
        If False, returns detailed device information. Defaults to True.

  Returns:
    A list of paired device names (if `only_name` is True) or a list of
    dictionaries containing detailed device information.
  """
  paired_devices = ad.mbs.btGetPairedDevices()
  if only_name:
    return list(
        map(lambda paired_info: paired_info['Name'], paired_devices))

  return [
      bt_data.PairedDeviceInfo.from_dict(pair_info_dict)
      for pair_info_dict in paired_devices]


def set_fast_pair_halfsheet(ad: android_device.AndroidDevice, enabled: bool):
  """Enables/disables fastpair setting.

  The halfsheet can pop up if a Fast Pair provider device is advertising nearby,
  it can lead to flakiness of UI layer tests. We can disable it by
  pass `enabled=False` to this method. (Or `enabled=True` to enable it)
  """
  ad.log.info(
      '%s Fast Pair Halfsheet.',
      ('Enable' if enabled else 'Disable'))

  flags = [
      'default_device_notification_enabled',
      'fast_pair_half_sheet_support',
      'fast_pair_half_sheet_wear_os',
  ]
  values = ['true' if enabled else 'false'] * len(flags)
  types = ['boolean'] * len(flags)
  ad.adb.shell([
      'am', 'broadcast',
      '-a', 'com.google.android.gms.phenotype.FLAG_OVERRIDE',
      '--es', 'package', 'com.google.android.gms.nearby',
      '--es', 'user', r'\*',
      '--esa', 'flags', ','.join(flags),
      '--esa', 'values', ','.join(values),
      '--esa', 'types', ','.join(types),
      'com.google.android.gms'])
  ad.adb.shell([
      'am', 'broadcast',
      '-a', 'com.google.android.gms.gcm.ACTION_TRIGGER_TASK',
      '-e', 'component',
      'com.google.android.gms/.phenotype.service.sync.PhenotypeConfigurator',
      '-e', 'tag', 'oneoff'])

  # Waits for phenotype sync.
  time.sleep(10)
  ad.reboot()


def set_name(ad: android_device.AndroidDevice, name: str) -> str:
  """Set the (Bluetooth) name of device.

  To use this function, the device need to support MBS (Mobly bundled snippets).

  Args:
    ad: The Android device object.
    name: The name to set as (Bluetooth) name.

  Returns:
    The (Bluetooth) name after set.
  """
  ad.mbs.btSetName(name)
  return get_name(ad)


def toggle_bluetooth(
    ad: android_device.AndroidDevice, enabled: bool = True) -> None:
  """Enables or disables Bluetooth on an Android device.

  Args:
    ad: The Android device object.
    enabled: True to enable Bluetooth, False to disable it.

  RuntimeError: If Bluetooth could not be toggled successfully. The error
      message includes the attempted state ('enabled' or 'disabled'),
      return code, and command output for troubleshooting.
  """
  status = 'enable' if enabled else 'disable'
  cmd = f'svc bluetooth {status}'
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(cmd)
  stdout = stdout.strip()
  # Expect 'disable: Success' or 'enable: Success'
  if ret_code == 0 and any([
      'Success' in stdout,
      stdout in {
          'Enabling Bluetooth',  # BDS's output
          '',  # SDK version < 33 (b/297539822#comment4)
      }]):
    return

  ad.log.warning(
      'Failed to toggle bluetooth with enabled=%s (rt=%s):\n%s\n',
      enabled, ret_code, stdout)

  raise RuntimeError(
      f'Failed in toggling bluetooth (enabled={enabled}) '
      f'with stdout: "{stdout}"')


def unbond_device(
    ad: android_device.AndroidDevice,
    name_or_mac: str,
    ignore_not_exist: bool = True,
    wait_time_sec: float = 3) -> bool:
  """Unbonds the BT device by its' name or MAC address.

  This operation requires DUT to be initialized with SL4A service.

  Args:
    ad: The Android device object.
    name_or_mac: Name or MAC of BT device to be unbonded.
    ignore_not_exist: True to ignore the case that if the target BT to be
        unbondeddoes not exist.

  Returns:
    True iff the target BT device is unbonded successfully.
  """
  for bt_name, bonded_device_info in ad.bt.bonded_devices.items():
    if name_or_mac in {bt_name, bonded_device_info.mac_addr}:
      ad.sl4a.bluetoothUnbond(bonded_device_info.mac_addr)
      ad.log.debug(
          'Sleep %ss for unbond action to become active...', wait_time_sec)
      time.sleep(wait_time_sec)
      name_or_mac_set = set()
      for bt_name, bonded_device_info in ad.bt.bonded_devices.items():
        name_or_mac_set.add(bt_name)
        name_or_mac_set.add(bonded_device_info.mac_addr)

      return name_or_mac not in name_or_mac_set

  ad.log.warning('Target device=%s does not exist!', name_or_mac)
  return ignore_not_exist
