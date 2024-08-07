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

"""Utility used in general operations of Phone."""

import dataclasses
import datetime
from functools import cache
import logging
import os
import re
import shutil
import sys
from subprocess import Popen, PIPE
import time

import bttc
from bttc import constants
from bttc import core
from bttc import errors
from bttc import general_data
from bttc.cli.constants import warning
from bttc.profiles.hfp import hfp_data
from bttc.utils import device_factory
from bttc.utils import key_events_handler
from bttc.utils import log_parser
from bttc.utils import pixellogger_utils
from bttc.utils import typing_utils
from bttc.utils.ui_pages import system as system_ui
from mobly import utils

from mobly.controllers import android_device
from mobly.controllers.android_device_lib import adb
from mobly.controllers.android_device_lib.errors import DeviceError

import functools
import shlex
from typing import (
    Any, Callable, Generator, Iterator, Protocol, TypeAlias, Union)


AUTO_LOAD = True
ANDROID_DEVICE: TypeAlias = android_device.AndroidDevice
BINDING_KEYWORD = "gm"


_ActivityRecord = general_data.ActivityRecord

# Default timeout for adb shell command.
_ADB_SHELL_TIMEOUT_SEC = constants.ADB_SHELL_TIMEOUT_SEC

# Logcat message timestamp format
_LOGCAT_DATETIME_FMT = constants.LOGCAT_DATETIME_FMT

# Pattern to match message of logcat service.
_LOGCAT_MSG_PATTERN = constants.LOGTCAT_MSG_PATTERN

# Command to retrieve SDK information.
_CMD_GET_SDK_VERSION = "getprop ro.build.version.sdk"

# The index of the setStreamVolume functio
_FUNC_IDX_SETSTREAMVOL = '10'


class DeviceConfig:
  """Utility class to handle device_config of DUT."""

  SettingPattern = re.compile(
      r'^(?P<setting_name>[ ._a-zA-Z0-9]+)='
      r'(?P<setting_value>.*)$')

  class Namespace:
    """Namespace of device_config."""

    @dataclasses.dataclass
    class Setting:
      name: str
      value: str
      err: str = ""

    class SettingIter:
      def __init__(self, setting_info: list[str]):
        self._setting_info = setting_info

      def __iter__(self) -> Iterator:
        return self

      def __next__(self):
        if self._setting_info:
          next_setting_str = self._setting_info.pop(0).strip()
          if next_setting_str:
            mth = DeviceConfig.SettingPattern.match(next_setting_str)
            if not mth:
              return DeviceConfig.Namespace.Setting(
                  name=None,
                  value=None,
                  err=f'Unexpected setting: {next_setting_str}')
            return DeviceConfig.Namespace.Setting(
                name=mth['setting_name'], value=mth['setting_value'])

          raise StopIteration

    def __init__(self, ad: typing_utils.AdbDevice, namespace: str):
      self._ad = ad
      self._namespace = namespace

    def __getitem__(
      self, setting_or_slice: str | slice
    ) -> str | list["DeviceConfig.Namespace.Setting"]:
      """Accesses setting value of current namespace."""
      if isinstance(setting_or_slice, slice):
        return list(self)[setting_or_slice]

      setting_value = device_config_get(
          self._ad, self._namespace, setting_or_slice)
      return DeviceConfig.Namespace.Setting(
          name=setting_or_slice, value=setting_value)

    def __setitem__(self, setting: str, value: str):
      """Put setting value of current namespace."""
      device_config_put(self._ad, self._namespace, setting, value)

    def __iter__(self) -> Iterator:
      """Iterates the settings of current namespace."""
      return DeviceConfig.Namespace.SettingIter(
          self._ad.adb.shell(f"device_config list {self._namespace}")
              .decode()
              .split("\n"))

  def __init__(self, ad: typing_utils.AdbDevice):
    self._ad = ad
    self._sync_disabled_for_tests: str | None = None

  @cache
  def namespaces(self) -> set[str]:
    """Gets namespaces of device_config."""
    return set(device_config_list_namespaces(self._ad))

  def __getattr__(self, namespace):
    if namespace not in self.namespaces():
      raise Exception(f"Namespace={namespace} does not exist!")

    return DeviceConfig.Namespace(self._ad, namespace)

  @property
  def sync_disabled_for_tests(self) -> str:
    """

    Modifies bulk property setting behavior for tests. When in one of the
    disabled modes this ensures that config isn't overwritten. This property is
    one of:
        "none": Sync is not disabled. A reboot may be required to restart
          syncing.
        "persistent": Sync is disabled, this state will survive a reboot.
        "until_reboot": Sync is disabled until the next reboot.
    """
    if self._sync_disabled_for_tests:
      return self._sync_disabled_for_tests

    shell_output = self._ad.adb.shell(
        'device_config get_sync_disabled_for_tests').decode().strip()
    self._sync_disabled_for_tests = shell_output
    return self._sync_disabled_for_tests

  @sync_disabled_for_tests.setter
  def sync_disabled_for_tests(self, value: str):
    value = value.strip()
    stdout, _, ret_code = bttc.safe_adb_shell(self._ad)(
        f"device_config set_sync_disabled_for_tests {value}")

    if ret_code != 0:
      self._ad.log.error(
          'Failed to set "sync_disabled_for_tests" with value="%s"', value)
      raise adb.Error(f'Stdout: {stdout} (rt={ret_code})')

    self._sync_disabled_for_tests = value


class Props:
  """Utility class to handle system property of DUT."""

  @dataclasses.dataclass
  class Prop:
    key: str
    val: str
    err: str = ""

    def __str__(self):
      if self.err:
        return self.err

      return f'[{self.key}]=[{self.val}]'

    def __repr__(self):
      return self.__str__()

  class PropIter:
    def __init__(self, property_info: list[str]):
      self._property_info = property_info
      self._prop_pattern = re.compile(r'^\[(?P<key>.*)]: \[(?P<val>.*)]$')

    def __iter__(self) -> Iterator:
      return self

    def __next__(self):
      if self._property_info:
        # e.g. '[zygote.critical_window.minute]: [10]'
        next_property_str = self._property_info.pop(0).strip()
        if next_property_str:
          mth = self._prop_pattern.match(next_property_str)
          if not mth:
            return Props.Prop(
                key=None,
                val=None,
                err=f'Unexpected property: {next_property_str}')
          return Props.Prop(key=mth['key'], val=mth['val'])

      raise StopIteration

  def __init__(self, ad: ANDROID_DEVICE):
    self._ad: ANDROID_DEVICE = ad

  def __getitem__(self, key: str | slice) -> str | list:
    """Accesses system property as `key`."""
    if isinstance(key, slice):
      return list(self)[key]

    return self._ad.adb.getprop(key)

  def __setitem__(self, key: str, value: str):
    """Sets system property as `key` to be `value`."""
    self._ad.adb.shell(f'setprop {key} {value}')

  def __iter__(self) -> Iterator:
    """Iterates the system propery."""
    return Props.PropIter(
        self._ad.adb.shell('getprop').decode().split('\n'))

  def grep(self, pattern: str) -> list[Prop]:
    """Greps the system properties.

    If your pattern starts with 'r:', it will be treated as regular expression.

    Args:
      pattern: Pattern to match names of system properties.

    Returns:
      Matched system propery list.
    """
    if pattern.startswith('r:'):
      re_pattern_str = pattern[2:]
      re_pattern_obj = re.compile(re_pattern_str)
      return [
          prop for prop in self if prop.key and re_pattern_obj.search(prop.key)]

    return [
        prop for prop in self if prop.key == pattern]


class Settings:
  """Utility class to handle settings of DUT."""

  SettingPattern = re.compile(
      r'^(?P<setting_name>[:/ ,._a-zA-Z0-9]+)='
      r'(?P<setting_value>.*)$')

  def __init__(self, ad: typing_utils.AdbDevice):
    self._ad = ad

  @property
  def g(self):
    return Settings.Namespace(self._ad, 'global')

  @property
  def secure(self):
    return Settings.Namespace(self._ad, 'secure')

  @property
  def system(self):
    return Settings.Namespace(self._ad, 'system')

  class Namespace:
    """Namespace of settings.

    Namespace is one of {system, secure, global}, case-insensitive
    """
    @dataclasses.dataclass
    class Setting:
      name: str
      value: str
      err: str = ""

    class SettingIter:
      def __init__(self, setting_info: list[str]):
        self._setting_info = setting_info

      def __iter__(self) -> Iterator:
        return self

      def __next__(self):
        if self._setting_info:
          next_setting_str = self._setting_info.pop(0).strip()
          if next_setting_str:
            mth = Settings.SettingPattern.match(next_setting_str)
            if not mth:
              return Settings.Namespace.Setting(
                  name=None,
                  value=None,
                  err=f'Unexpected setting: {next_setting_str}')
            return Settings.Namespace.Setting(
                name=mth['setting_name'], value=mth['setting_value'])

          raise StopIteration

    def __init__(self, ad: typing_utils.AdbDevice, namespace: str):
      self._ad = ad
      self._namespace = namespace

    def __getitem__(
      self, setting_or_slice: str | slice
    ) -> str | list["Settings.Namespace.Setting"]:
      """Accesses setting value of current namespace."""
      if isinstance(setting_or_slice, slice):
        return list(self)[setting_or_slice]

      setting_value = settings_get(
          self._ad, self._namespace, setting_or_slice)
      return Settings.Namespace.Setting(
          name=setting_or_slice, value=setting_value)

    def __setitem__(self, setting: str, value: str):
      """Put setting value of current namespace."""
      settings_put(self._ad, self._namespace, setting, value)

    def __iter__(self) -> Iterator:
      """Iterates the settings of current namespace."""
      return Settings.Namespace.SettingIter(
          self._ad.adb.shell(f"settings list {self._namespace}")
              .decode()
              .split("\n"))


class LogcatSearchStrategy(Protocol):
  """Logcat searching strategy.

  Attributes:
    log_pattern: Log pattern to search in logcat messages.
    start_device_time: Begin time to start searching.
    stop: True means the searching is completed.
  """

  def __init__(
      self,
      begin_device_time: str,
      log_pattern: str,
      end_device_time: str | None = None):
    try:
      self._start_device_time = datetime.datetime.strptime(
          begin_device_time, _LOGCAT_DATETIME_FMT)
      self._end_device_time = (
          datetime.datetime.strptime(
              end_device_time, _LOGCAT_DATETIME_FMT) if end_device_time
          else None)
    except ValueError as ex:
      logging.error('Invalid device time as "%s"!', begin_device_time)
      raise ex

    self._log_pattern = log_pattern
    self._stop = False

  @property
  def log_pattern(self) -> str:
    """Log pattern to search in logcat messages."""
    return self._log_pattern

  @property
  def start_device_time(self) -> datetime.datetime:
    """The device time to start searching."""
    return self._start_device_time

  @property
  def end_device_time(self) -> datetime.datetime:
    """The device time to stop searching."""
    return self._end_device_time

  @property
  def stop(self) -> bool:
    """True means the searching is done."""
    return self._stop

  def matcher(self, line) -> Any:
    """Checks if the given line matches the log pattern."""
    return re.search(self.log_pattern, line)

  def do_search(self, line: str, device_time: datetime.datetime) -> Any:
    """Searches the interested line."""
    ...

  def search(self, line: str) -> Any:
    """Matches the input line to checks if it is wanted."""
    time_matcher = _LOGCAT_MSG_PATTERN.match(line)
    if time_matcher:
      log_device_time = datetime.datetime.strptime(
          time_matcher.group('datetime'), _LOGCAT_DATETIME_FMT)
      return self.do_search(line, log_device_time)

    return None


class LogcatSearchToEnd(LogcatSearchStrategy):
  """Searches logcat message with given pattern until the last line."""

  def search(self, line: str) -> Any:
    matcher = _LOGCAT_MSG_PATTERN.match(line)
    post_start_time = False
    if matcher:
      log_device_time = datetime.datetime.strptime(
          matcher.group('datetime'), _LOGCAT_DATETIME_FMT)
      if not post_start_time and log_device_time >= self.start_device_time:
        post_start_time = True

      if (
          post_start_time and
          re.search(self.log_pattern, line) is not None):
        return line

    return ''


class LogcatSearchAfter(LogcatSearchStrategy):
  """Searches logcat message after given device time."""

  def __init__(self, begin_device_time: str):
    super().__init__(
        begin_device_time=begin_device_time,
        log_pattern='')

  def search(self, line: str) -> Any:
    matcher = _LOGCAT_MSG_PATTERN.match(line)
    if matcher:
      log_device_time = datetime.datetime.strptime(
          matcher.group('datetime'), _LOGCAT_DATETIME_FMT)
      if log_device_time >= self.start_device_time:
        return line

    return ''


class LogcatSearchAfterWithMatcher(LogcatSearchStrategy):
  """Searches after given device time and returns matcher object."""

  def __init__(self, begin_device_time: str, log_pattern: str):
    super().__init__(
        begin_device_time=begin_device_time,
        log_pattern=log_pattern)

  def search(self, line: str) -> Any:
    if self.stop:
      return None

    time_matcher = _LOGCAT_MSG_PATTERN.match(line)
    if time_matcher:
      log_device_time = datetime.datetime.strptime(
          time_matcher.group('datetime'), _LOGCAT_DATETIME_FMT)

      matcher = self.matcher(line)
      if log_device_time >= self.start_device_time and matcher:
        self._stop = True
        return matcher

    return None


class LogcatSearchRange(LogcatSearchStrategy):
  """Searches after given start time and stop before end time."""

  def __init__(
      self, begin_device_time: str, end_device_time: str, log_pattern: str):
    super().__init__(
        begin_device_time=begin_device_time,
        log_pattern=log_pattern,
        end_device_time=end_device_time)

  def do_search(self, line: str, device_time: datetime.datetime) -> Any:
    if self.stop or device_time < self.start_device_time:
      return None

    if device_time > self.end_device_time:
      self._stop = True
      return None

    return line if self.matcher(line) else None


class LogcatSearchUntil(LogcatSearchStrategy):

  def search(self, line: str) -> Any:
    matcher = _LOGCAT_MSG_PATTERN.match(line)
    if matcher:
      log_device_time = datetime.datetime.strptime(
          matcher.group('datetime'), _LOGCAT_DATETIME_FMT)

      if log_device_time > self.start_device_time:
        self._stop = True
        return ''

      if re.search(self._log_pattern, line):
        return line

    return ''


class GModule(core.UtilBase):
  """Utility class to hold extended functions define in this module."""

  NAME = BINDING_KEYWORD
  DESCRIPTION = (
      'Utility to hold device core operations such as retrieving device '
      'information etc.')

  def __init__(self, ad: ANDROID_DEVICE):
    """Initializes the GModule utility class.

    Args:
        ad:  The Android device object to control.
    """
    self._ad: ANDROID_DEVICE = ad
    self.device_config = DeviceConfig(self._ad)
    self._bind(disable_airplane_mode)
    self._bind(dumpsys)
    self._bind(dump_bugreport)
    self._bind(enable_airplane_mode)
    self._bind(follow_logcat)
    self._bind(follow_logcat_within)
    self._bind(get_call_state)
    self._bind(get_current_activity)
    self._bind(get_device_time)
    self._bind(get_ui_xml)
    self._bind(get_all_volume)
    self._bind(get_volume)
    self._bind(is_apk_installed)
    self._bind(is_sim_state_loaded)
    self._bind(logcat_filter)
    self.props = Props(self._ad)
    self._bind(push_file)
    self._bind(push_non_persistent_property)
    self._bind(search_logcat_after)
    self._bind(settings_get)
    self._bind(settings_put)
    self._bind(set_volume)
    self.settings = Settings(self._ad)
    self.shell = bttc.safe_adb_shell(ad)
    self._bind(take_screenshot)
    self._pixellogger_broker: pixellogger_utils.Broker | None = None

  @property
  def airplane_mode(self) -> bool:
    """Gets the current airplane mode status of the device.

    Returns:
        bool: True if airplane mode is enabled, False otherwise.
    """
    return get_airplane_mode(self._ad)

  @airplane_mode.setter
  def airplane_mode(self, new_value: bool):
    """Set airplane mode."""
    if new_value:
      self.enable_airplane_mode()
    else:
      self.disable_airplane_mode()

  @property
  def build_id(self) -> str:
    return str(self.props['ro.build.id'])

  @property
  def call_state(self) -> str:
    return self.get_call_state()

  @property
  def chipset(self) -> str:
    return self.props['gsm.version.ril-impl']

  @property
  def current_activity(self) -> _ActivityRecord:
    return self.get_current_activity()

  @property
  def device_time(self) -> str:
    return self.get_device_time()

  @property
  def device_datetime(self) -> datetime.datetime:
    return self.get_device_time(to_datetime=True)

  @property
  def hardware(self) -> str:
    return str(self.props['ro.boot.hardware'])

  @property
  def pixellogger_broker(self) -> pixellogger_utils.Broker:
    if self._pixellogger_broker is None:
      self._pixellogger_broker = pixellogger_utils.Broker(self._ad)

    return self._pixellogger_broker

  @property
  def sdk(self) -> str:
    return get_sdk_version(self._ad)

  @property
  def setting_dnd(self) -> Settings.Namespace.Setting:
    """Gets setting of "Do not Disturb" (DnD)."""
    return self.settings.g['zen_mode']

  @setting_dnd.setter
  def setting_dnd(self, value: bool) -> Settings.Namespace.Setting:
    """Set setting of "Do not Disturb" (DnD)."""
    system_ui.set_do_not_disturb(self._ad, value)

  @property
  def sim_loaded(self):
    return self.is_sim_state_loaded()

  @property
  def sim_operator(self):
    return get_sim_operator(self._ad)

  def quick_setting_page(self):
    return go_bt_quick_setting_page(self._ad)

  def volume_down(self):
    self.dut.ke.key_volume_down()

  def volume_up(self):
    self.dut.ke.key_volume_up()


def bind(
    ad: Union[ANDROID_DEVICE, str],
    depress_error: bool = True,
    init_mbs: bool = False,
    init_sl4a: bool = False,
    init_snippet_uiautomator: bool = False,
    init_tl4a: bool = False,
) -> ANDROID_DEVICE:
  """Binds the input device with functions defined in current module.

  Sample Usage:
  ```python
  >>> from bttc import general_utils
  >>> ad = general_utils.bind('07311JECB08252', init_mbs=True, init_sl4a=True)
  >>> ad.gm.sim_operator
  'Chunghwa Telecom'
  >>> ad.gm.call_state
  'IDLE'
  ```

  Args:
      ad: The Android device object or a device identifier.
      depress_error: If True, depress the thrown Exception during binding.
      init_mbs: If True, initializes the MBS library.
      init_sl4a: If True, initializes SL4A.
      init_snippet_uiautomator: If True, initializes tools for UI scripting.
      init_tl4a: If True, initializes TL4A.

  Returns:
      The prepared Android device object, ready for use with the module's
      utility functions.
  """
  device = device_factory.get(
      ad,
      init_mbs=init_mbs,
      init_sl4a=init_sl4a,
      init_snippet_uiautomator=init_snippet_uiautomator,
      init_tl4a=init_tl4a,
  )
  try:
    device.load_config({BINDING_KEYWORD: GModule(device)})
  except DeviceError as ex:
    if depress_error:
      warning(ex)
    else:
      raise ex
  device.ke = key_events_handler.KeyEventHandler(device)

  return device


_CMD_GET_AIRPLANE_MODE_SETTING = "settings get global airplane_mode_on"


def disable_airplane_mode(
    device: typing_utils.AdbDevice, wait_secs: float = 1):
  """Disables airplane mode on device.

  Args:
    device: Adb like device.
    wait_secs: The amount of time to wait after sending the airplane
      mode broadcast.
  """
  if not get_airplane_mode(device):
    device.log.debug('Airplane mode is already disabled!')
    return

  device.adb.shell(
      ['settings', 'put', 'global', 'airplane_mode_on', '0'],
      timeout=_ADB_SHELL_TIMEOUT_SEC)

  device.adb.shell(
      [
          'am',
          'broadcast',
          '-a',
          'android.intent.action.AIRPLANE_MODE',
          '--ez',
          'state',
          'true',
      ],
      timeout=_ADB_SHELL_TIMEOUT_SEC,
  )
  time.sleep(wait_secs)


def enable_airplane_mode(
    device: typing_utils.AdbDevice, wait_secs: float = 1):
  """Enables airplane mode on device.

  Args:
    device: Adb like device.
    wait_secs: The amount of time to wait after sending the airplane
      mode broadcast.
  """
  if get_airplane_mode(device):
    device.log.debug('Airplane mode is already enabled!')
    return

  device.adb.shell(
      ['settings', 'put', 'global', 'airplane_mode_on', '1'],
      timeout=_ADB_SHELL_TIMEOUT_SEC)

  device.adb.shell(
      [
          'am',
          'broadcast',
          '-a',
          'android.intent.action.AIRPLANE_MODE',
          '--ez',
          'state',
          'true',
      ],
      timeout=_ADB_SHELL_TIMEOUT_SEC,
  )
  time.sleep(wait_secs)


def get_airplane_mode(device: typing_utils.AdbDevice) -> bool:
  """Gets the state of airplane mode.

  Args:
    device: Adb like device.

  Raises:
    adb.Error: Fail to execute adb command.
    ValueError: The output of adb command is unexpected.

  Returns:
    True iff the airplane mode is on.
  """
  shell_output = (
      device.adb.shell(_CMD_GET_AIRPLANE_MODE_SETTING)
      .decode(constants.ADB_SHELL_CMD_OUTPUT_ENCODING)
      .strip())
  device.log.info("Current airplane mode is %s", shell_output)
  try:
    return bool(int(shell_output))
  except ValueError as ex:
    device.log.warning("Unknown adb output=%s", ex)
    raise


def get_call_state(device: typing_utils.AdbDevice) -> hfp_data.CallStateEnum:
  """Gets call state from dumpsys telecom log.

  For this function to work, we expect below log snippet from given log
  content:

  Call state is IDLE:
  ```
  mCallAudioManager:
    All calls:
    Active dialing, or connecting calls:
    Ringing calls:
    Holding calls:
    Foreground call:
    null
  ```

  Call state is ACTIVE if there is a single call:
  ```
  mCallAudioManager:
    All calls:
      TC@1
    Active dialing, or connecting calls:
      TC@1
    Ringing calls:
    Holding calls:
    Foreground call:
    [Call id=TC@1, state=ACTIVE, ...
  ```

  Call state is RINGING if there is two calls:
  ```
  mCallAudioManager:
    All calls:
      TC@1
      TC@2
    Active dialing, or connecting calls:
      TC@1
    Ringing calls:
      TC@2
    Holding calls:
    Foreground call:
    [Call id=TC@1, state=ACTIVE, ...
  ```

  Args:
    device: Adb like device.

  Returns:
    Call state of the device.

  Raises:
    adb.Error: If the output of adb commout is not expected.
  """
  output = dumpsys(device, "telecom", "mCallAudioManager", "-A11")
  pattern = r"(Ringing) calls:\n\s+TC@\d|Call id=.+state=(\w+)|null"
  match = re.search(pattern, output)
  if match is None:
    raise adb.Error("Failed to execute command for dumpsys telecom")

  return hfp_data.CallStateEnum.from_str(
      (match.group(1) or match.group(2) or "IDLE").upper())


def get_device_time(
  device: typing_utils.AdbDevice, to_datetime: bool = False
) -> str | datetime.datetime:
  """Gets device epoch time and transfer to logcat timestamp format."""
  device_time_str = (
      device.adb.shell('date +"%m-%d %H:%M:%S.000"').decode().splitlines()[0]
  )
  if to_datetime:
    dt_format = constants.LOGCAT_DATETIME_FMT
    return datetime.datetime.strptime(device_time_str, dt_format).replace(
        year=datetime.datetime.now().year)

  return device_time_str


@functools.lru_cache
def get_sdk_version(device: typing_utils.AdbDevice) -> int:
  """Gets SDK version of given device.

  Args:
    device: Adb like device.

  Returns:
    SDK version of given device.
  """
  return int(device.adb.shell(shlex.split(_CMD_GET_SDK_VERSION)))


def get_sim_operator(ad: ANDROID_DEVICE) -> str:
  """Gets SIM operator.

  Args:
    ad: Android phone device object.

  Returns:
    SIM Operator or empty string if no SIM card.
  """
  return ad.adb.getprop("gsm.operator.alpha").split(",")[0]


def go_bt_quick_setting_page(ad: ANDROID_DEVICE):
  """Opens Quick Settings."""
  ad.adb.shell(["cmd", "statusbar", "expand-settings"])


def device_config_get(
    ad: typing_utils.AdbDevice, namespace: str, setting: str) -> str:
  """Gets setting from a given device_config namespace.

  Args:
    ad: Adb like device.
    namespace: Namespace to query for.
    setting: The setting name.

  Returns:
    The corresponding setting value.

  Raises:
    adb.Error: Fail to get setting from given namespace.
  """
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(
      f"device_config get {namespace} {setting}"
  )
  if ret_code != 0:
    raise adb.Error(
        f"Failed to retrieve setting={setting} (rt={ret_code}): "
        f'{stdout or "?"}')

  return stdout.strip()


def device_config_list(ad: typing_utils.AdbDevice, namespace: str) -> list[str]:
  """Lists all settings of the given namespace.

  Args:
    ad: Adb like device.
    namespace: Namespace to list settings.

  Returns:
    All settings of given namespace.

  Raises:
    adb.Error: Fail to list settings of given device_config namespace.
  """
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(
      f"device_config list {namespace}")
  if ret_code != 0:
    raise adb.Error(
        'Failed to retrieve settings of device_config '
        f'namespace={namespace} (rt={ret_code}): {stdout or "?"}'
    )

  return [n.strip() for n in stdout.split("\n") if n.strip()]


def device_config_list_namespaces(ad: typing_utils.AdbDevice) -> list[str]:
  """Lists namespaces of device_config.

  Args:
    ad: Adb like device.

  Returns:
    List of device_config namespace.

  Raises:
    adb.Error: Fail to list device_config namespaces.
  """
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(
      'device_config list_namespaces')
  if ret_code != 0:
    raise adb.Error(
        f'Failed to retrieve namespaces of device_config (rt={ret_code}): '
        f'{stdout or "?"}'
    )

  return [n.strip() for n in stdout.split("\n") if n.strip()]


def device_config_put(
    ad: typing_utils.AdbDevice, namespace: str, setting: str, value: str
):
  """Put setting into a given device_config namespace.

  Args:
    ad: Adb like device.
    namespace: Namespace to process.
    setting: The setting name.

  Raises:
    adb.Error: Fail to put device_config setting.
  """
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(
      f"device_config put {namespace} {setting} {value}")
  if ret_code != 0:
    raise adb.Error(
        f'Failed to put "{setting}={value}" in namespace={namespace}'
        f'(rt={ret_code}): {stdout or "?"}'
    )


def dumpsys(
    ad: typing_utils.AdbDevice,
    service: str = 'bluetooth_manager',
    keyword: str = '',
    grep_argument: str = ''
) -> str:
  """Retrieves and filters dumpsys output for a specified service.

  Args:
    ad: An Adb-like device object.
    service: The name of the service to query (e.g., 'bluetooth_manager').
    keyword: A keyword to filter the dumpsys output.
    grep_argument: Additional grep arguments for filtering.

  Returns:
    The filtered dumpsys output.

  Raises:
    UnicodeDecodeError: If the default decoding of the output fails.
  """
  command = f'dumpsys {shlex.quote(service)}'
  if keyword or grep_argument:
    command += f' | grep {grep_argument} {shlex.quote(keyword)}'

  return ad.adb.shell(shlex.split(command)).decode()


def dump_bugreport(
    ad: typing_utils.AdbDevice,
    host_destination: str = None,
    file_name: str = None) -> str:
  """Dumps the bugreport to the given path.

  Args:
    ad: An Adb-like device object.
    host_destination: Directory path at host to dump the bugreport.
    file_name: The name of bugreport file.

  Returns:
    The path of dumped bugreport.
  """
  dumped_bugreport_path = ad.take_bug_report()
  host_destination = host_destination or ad.log_path
  timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
  file_name = file_name or f'bugreport_{timestamp}.zip'
  final_bugreport_path = os.path.join(host_destination, file_name)
  shutil.move(dumped_bugreport_path, final_bugreport_path)
  return final_bugreport_path


def follow_logcat(
    ad: typing_utils.AdbDevice,
    stop_callback: Callable[..., bool],
    wait_time_sec: float = 2.0,
    logcat_args: str | None = None,
) -> Generator[str, None, None]:
  """Tail-follows the logcat and stops by given signal.

  Args:
    ad: Adb like object.
    stop_callback: A callback function to obtain stop signal. If True is
      returned, the generator will terminate.
    wait_time_sec: Waiting time when no new line generated from the logcat
      file.
    logcat_args: Argument to logcat command.

  Returns:
    The generator to tail follow logcat file.
  """
  if logcat_args:
    proc = None
    shell_cmd = f'adb -s {ad.serial} shell logcat {logcat_args}'
    proc = Popen(
        shell_cmd, shell=True,
        stdout=PIPE)

    # Filtering logcat line(s) before current device time.
    last_line_bin = None
    last_line = None
    logcat_filter = LogcatSearchAfter(ad.gm.device_time)
    while True:
      try:
        last_line_bin = proc.stdout.readline()
        last_line = last_line_bin.decode(errors="ignore")
      except KeyboardInterrupt:
        break
      except Exception as ex:
        logging.warning(f'Error: {ex}')
        break

      if logcat_filter.search(last_line):
        yield last_line
        break

    while not stop_callback(last_line):
      try:
        last_line = proc.stdout.readline().decode(errors="ignore").strip()
      except KeyboardInterrupt:
        break
      except Exception as ex:
        logging.warning(f'Error: {ex}')
        continue

      if not last_line:
        time.sleep(wait_time_sec)
        continue

      yield last_line

    if proc:
      proc.kill()
  else:
    with open(ad.adb_logcat_file_path, "r", errors="replace") as logcat_fo:
      # Seek the end of the file
      logcat_fo.seek(0, os.SEEK_END)

      last_line = None
      # start infinite loop to follow logcat file.
      while not stop_callback(last_line):
        last_line = logcat_fo.readline()
        if not last_line:
          time.sleep(wait_time_sec)
          continue

        last_line = last_line.rstrip()
        yield last_line


def follow_logcat_within(
    ad: typing_utils.AdbDevice, time_sec: float = 5,
    wait_time_sec: float = 2.0,
    logcat_args: str | None = None,
) -> Generator[str, None, None]:
  """Tail-follows the logcat for certain time.

  Args:
    ad: Adb like object.
    time_sec: Time to stop tail-following logcat.
    wait_time_sec: Waiting time when no new line generated from the logcat
        file.
    logcat_args: Argument to logcat command.

  Returns:
    The generator to tail follow logcat file within given time.
  """
  start_time = datetime.datetime.now()

  def stop_callback(_):
    pass_time_sec = (datetime.datetime.now() - start_time).total_seconds()
    if pass_time_sec > time_sec:
      return True

    return False

  return follow_logcat(
      ad, stop_callback, wait_time_sec, logcat_args=logcat_args)


def get_current_activity(ad: typing_utils.AdbDevice) -> _ActivityRecord:
  """Gets current activity that is currently opened to the user.

  Args:
    ad: Adb like object.

  Returns:
    The current activity information.
  """
  adb_output = (
      ad.adb.shell(
          'dumpsys activity activities | grep ResumedActivity').decode())
  matcher = constants.ACTIVITY_RECORD_COMPILED_PATTERN.search(adb_output)
  if not matcher:
    raise ValueError(f'Unexpected adb output: {adb_output}')

  return _ActivityRecord(full_activity_path=matcher.group(1))


def get_ui_xml(ad: Any, xml_out_file_path: str) -> str:
  """Gets the XML object of current UI.

  Args:
    ad: Device to dump UI from.
    xml_out_file_path: The host file path to output current UI xml content.

  Returns:
    Current UI xml content.

  Raises:
    errors.MethodError: Fail to dump UI xml.
  """
  dump_xml_name = 'window_dump.xml'
  internal_dump_xml_path = f'/sdcard/{dump_xml_name}'
  ui_xml_content = None
  try:
    ui_xml_content = ad.ui.dump() or ''
  except AttributeError:
    pass

  if not ui_xml_content:
    ad.log.warning('Failed to retrieve UI xml from uiautomator!')
    ad.log.info('Trying `uiautomator dump`...')
    ad.adb.shell(
        f'test -f {internal_dump_xml_path} && rm {internal_dump_xml_path}'
        " || echo 'no need to clean exist dumped xml file'")
    shell_obj = bttc.safe_adb_shell(ad)

    last_rt = 0
    last_message = None
    for retry_num in range(5):
      shell_obj('uiautomator dump')
      stdout, stderr, rt = shell_obj(f'test -f {internal_dump_xml_path}')
      if rt != 0:
        # When the dumped xml file doesn't exist, we can try to recover it by
        #   wake up the device and dump again.
        ad.log.warning(
            'Dumped file=%s is missing (rt=%d): %s',
            internal_dump_xml_path, rt, stderr)
        ad.log.warning('Wake up the device to recover this issue...')
        ke_handler = key_events_handler.KeyEventHandler(ad)
        ke_handler.key_wakeup()
        ad.log.info('Collect UI xml again...(retry=%d)', retry_num + 1)
        last_rt = rt
        last_message = f'{stdout}\n{stderr}'
      else:
        break
    else:
      raise errors.MethodError(
          sys._getframe().f_code.co_name,
          f'Failed to retrieve XML content by uiautomator (rt={last_rt}):\n'
          f'{last_message}')
    ad.adb.pull(
        shlex.split(f'{internal_dump_xml_path} {xml_out_file_path}'))
    ui_xml_content = open(xml_out_file_path).read()
  else:
    with open(xml_out_file_path, 'w') as fo:
      fo.write(ui_xml_content)

  if not ui_xml_content:
    raise errors.MethodError(
        sys._getframe().f_code.co_name,
        'Failed to get XML content of current UI!')

  return ui_xml_content


def get_all_volume(
    ad: typing_utils.AdbDevice) -> dict[str, general_data.AudioStreamVolume]:
  """Gets all the types of volume setting.

  Args:
    ad: Device to retrieve volume setting.

  Returns:
    The settings of all audio volume types with key as name; value as settings.
  """
  stdout, _, ret_code = bttc.safe_adb_shell(ad)('dumpsys audio')

  if ret_code != 0:
    raise adb.Error(
        f'Failed to get volume with stdout: {stdout} (rt={ret_code})')

  return log_parser.parse_audio_dump_for_volume_info(stdout)


def get_volume(
    ad: typing_utils.AdbDevice,
    volume_type: general_data.VolumeType) -> general_data.VolumeSetting:
  """Gets the setting of a certain volume type.

  Args:
    ad: Device to retrieve volume setting.
    volume_type: Volume type to query on.

  Returns:
    The current volume setting.
  """
  key = volume_type.m.key or volume_type.m.stream_type
  shell_cmd = f'settings get system {key}'
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(shell_cmd)
  if ret_code != 0:
    raise adb.Error(
        f'Failed to get volume with stdout: {stdout} (rt={ret_code})')

  stdout = stdout.strip()
  if stdout == 'null':
    raise adb.Error(
        f'Failed to get volume by command: "{shell_cmd}"')

  volume_level = int(stdout.strip())
  return general_data.VolumeSetting(
      level=volume_level,
      is_max=volume_level >= volume_type.m.max,
      is_min=volume_level <= volume_type.m.min)


def is_apk_installed(
    device: typing_utils.AdbDevice, package_name: str, is_full: bool = False
) -> bool:
  """Checks if the given apk is installed.

  Below is the output of partial package:
  ```
  # pm list packages
  ...
  package:com.google.android.GoogleCamera
  ```
  Here the partial package name will be:
  'com.google.android.GoogleCamera'

  Below is the output of full package:
  ```
  # pm list packages -f
  ...
  package:/product/app/GoogleCamera/GoogleCamera.apk=com.google.android.GoogleCamera
  ```
  Here the full package name will be:
  '/product/app/GoogleCamera/GoogleCamera.apk=com.google.android.GoogleCamera'

  Args:
    device: Adb like device.
    package_name: APK package name.
    is_full: The given `package_name` is of full path if True. False means the
      `package_name` is partial.

  Returns:
    True iff the given APK package name installed.
  """
  command = (
      f'pm list packages {"-f" if is_full else ""} '
      f'| grep -w "package:{package_name}"'
  )
  stdout, _, ret_code = bttc.safe_adb_shell(device)(command)

  return ret_code == 0 and package_name in stdout


def is_sim_state_loaded(ad: typing_utils.AdbDevice) -> bool:
  """Checks if SIM state is loaded.

  This method checks the first SIM only.

  Below is the negative case:
  ```shell
  husky:/ # getprop gsm.sim.state
  ABSENT,NOT_READY
  ```

  The positive case:
  ```shell
  husky:/ # getprop gsm.sim.state
  LOADED,NOT_READY
  ```

  Returns:
    True if SIM state is loaded else False.
  """
  sim_state_info = ad.gm.props['gsm.sim.state']
  if not sim_state_info:
    logging.warning('Failed to get SIM state!')
    return False

  return sim_state_info.split(',')[0] == 'LOADED'


def logcat_filter(
    ad: typing_utils.AdbDevice,
    start_time: str | None = None,
    text_filter: str = '',
    return_matcher: bool = False) -> Any:
  """Returns logcat messages after a given time.

  This method calls from the logcat service file of `ad` and filters
  all logcat line prior to the start_time.

  Usage:
  ```python
  >>> dut = bttc.get('36121FDJG000GR')
  >>> device_time = dut.gm.device_time
  >>> # Conduct pairing with headset from DUT
  >>> dut.gm.logcat_filter(device_time, 'BOND_BONDING => BOND_BONDED')
  '...'
  ```

  Args:
    start_time: start time in string format of `_LOGCAT_DATETIME_FMT`.
    text_filter: only return logcat lines that include this string or regex.
    return_matcher: True to return matcher object instead.

  Returns:
    A logcat output or matcher object.

  Raises:
    ValueError Exception if start_time is invalid format.
  """
  searching_uitl_now = False
  if not start_time:
    searching_uitl_now = True
    start_time = datetime.datetime.now().strftime(_LOGCAT_DATETIME_FMT)

  logcat_response = ''
  if return_matcher:
    search_strategy = LogcatSearchAfterWithMatcher(start_time, text_filter)
  else:
    search_strategy = (
        LogcatSearchUntil(start_time, text_filter) if searching_uitl_now
        else LogcatSearchToEnd(start_time, text_filter))

  with open(ad.adb_logcat_file_path, 'r', errors='replace') as logcat_file:
    for line in logcat_file:
      returned_value = search_strategy.search(line)
      if return_matcher and returned_value:
        return returned_value

      if returned_value:
        logcat_response += line
      if search_strategy.stop:
        break

  return logcat_response


def push_file(
    ad: typing_utils.AdbDevice,
    src_file_path: str,
    dst_file_path: str,
    push_timeout_sec: int = 300,
    overwrite_existing: bool = True,
) -> bool:
  """Pushes a file from the host file system to an Android device (DUT).

  Args:
    ad: An Adb-like device object representing the DUT.
    src_file_path: The path to the file on the host.
    dst_file_path: The destination path on the Android device.
    push_timeout_sec: Maximum time to wait for the push operation (in seconds).
        Defaults to 300 seconds.
    overwrite_existing: If True, overwrites an existing file at the destination.
        If False, skips the push if the destination file exists.

  Returns:
    True if the file was pushed successfully, False otherwise.
  """
  src_file_path = os.path.expanduser(src_file_path)

  if not os.path.isfile(src_file_path):
    logging.warning("Source file %s does not exist!", src_file_path)
    return False

  if not overwrite_existing and ad.adb.path_exists(dst_file_path):
    logging.debug(
        "Skip pushing {} to {} as it already exists on device".format(
            src_file_path, dst_file_path))
    return True

  out = (
      ad.adb.push(
          [src_file_path, dst_file_path],
          timeout=push_timeout_sec).decode().rstrip())
  if "error" in out:
    logging.warning(
        "Failed to copy %s to %s: %s", src_file_path, dst_file_path, out
    )
    return False

  return True


def push_non_persistent_property(
    ad: typing_utils.AdbDevice,
    property_name: str, property_value: str) -> None:
  """Pushes non persistent property.

  Args:
    ad: An Adb-like device object representing the DUT.
    property_name: Name of property.
    property_value: Value of property.

  Raises:
    adb.AdbError: Failed in pushing the desired property.
  """
  if ad.gm.props[property_name] == property_value:
    logging.info('Property="%s" is already set!', property_name)
    return

  ad.adb.shell(
      f"'echo {property_name}={property_value} >> /data/local.prop'",
      shell=True)

  try:
    ad.adb.shell("'chmod 644 /data/local.prop'", shell=True)
  except adb.AdbError as ex:
    ad.log.error(
        f'Failed to push persistent property="{property_name}": {ex}')
    raise ex


def search_logcat_after(
    ad: typing_utils.AdbDevice,
    start_device_time: str,
    search_pattern: str,
    end_device_time: str | None = None,
) -> list[str]:
  """Search the logcat message with given pattern and after given device time.

  Args:
    ad: Adb like object.
    start_device_time: A string representing the device time (logcat timestamp
      format) from which to start searching.
    search_pattern: A regular expression or plain text string used to filter
      logcat messages. Matching messages will be included in the results. If
      empty string is given, all messages will be collected.
    end_device_time: A string representing the device time (logcat timestamp
      format) from which to stop searching. None means to search util the end
      of logcat messages.

  Returns:
    List of collected logcat message.
  """
  if all([
      start_device_time,
      search_pattern,
      end_device_time]):
    search_strategy = LogcatSearchRange(
        begin_device_time=start_device_time,
        log_pattern=search_pattern,
        end_device_time=end_device_time)
  else:
    search_strategy: LogcatSearchStrategy = (
        LogcatSearchToEnd(start_device_time, search_pattern) if search_pattern
        else LogcatSearchAfter(start_device_time))

  collected_messages = []
  with open(ad.adb_logcat_file_path, "r", errors="replace") as logcat_fo:
    for line in logcat_fo:
      if search_strategy.search(line):
        collected_messages.append(line.rstrip())

      if search_strategy.stop:
        break

  return collected_messages


def settings_get(
    ad: typing_utils.AdbDevice, namespace: str, setting: str) -> str:
  """Gets setting from a given namespace in device's settings.

  Args:
    ad: Adb like device.
    namespace: Namespace to query for.
    setting: The setting name.

  Returns:
    The corresponding setting value.

  Raises:
    adb.Error: Fail to get setting from given namespace.
  """
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(
      f"settings get {namespace} {setting}"
  )
  if ret_code != 0:
    raise adb.Error(
        f"Failed to retrieve setting={setting} (rt={ret_code}): "
        f'{stdout or "?"}')

  return stdout.strip()


def settings_put(
    ad: typing_utils.AdbDevice, namespace: str, setting: str, value: str
):
  """Put setting into a given namespace in device's settings.

  Args:
    ad: Adb like device.
    namespace: Namespace to process.
    setting: The setting name.

  Raises:
    adb.Error: Fail to put device_config setting.
  """
  stdout, _, ret_code = bttc.safe_adb_shell(ad)(
      f"settings put {namespace} {setting} {value}")
  if ret_code != 0:
    raise adb.Error(
        f'Failed to put "{setting}={value}" in namespace={namespace}'
        f'(rt={ret_code}): {stdout or "?"}'
    )


def set_volume(
    ad: typing_utils.AdbDevice,
    volume_type: general_data.VolumeType,
    level: int,
    sync_wait_sec: int = 2) -> str:
  """Sets the level of a certain volume type.

  Passes value out of boundary will be adjusted to boudary value.

  Via adb command (put) to update volume values in settings is not working.
  Need to use Android Interface Definition Language (AIDL) instead.
  Refer to: cs/frameworks/base/media/java/android/media/IAudioService.aidl
  for further information.

  Args:
    ad: Device to set the volume.
    volume_type: Volume type to qork on.
    level: Level to set in.
    sync_wait_sec: Time of second to wait after setting the volume level for the
      device to sync up.

  Returns:
    adb shell command return value.

  Raises:
    ValueError: Giving invalid level value.
  """
  if level < volume_type.m.min:
    raise ValueError(
        f'Level={level} is less than the minimum level from {volume_type.m}')
  elif level > volume_type.m.max:
    raise ValueError(
        f'Level={level} is higher than the maximum level from {volume_type.m}')

  shell_cmd = ' '.join([
      'service', 'call', 'audio', _FUNC_IDX_SETSTREAMVOL, 'i32',
      volume_type.m.stream_type, 'i32',
      str(level), 'i32', '1'])

  stdout, _, ret_code = bttc.safe_adb_shell(ad)(shell_cmd)
  if ret_code != 0:
    raise adb.Error(
        f'Failed to get volue with stdout: {stdout} (rt={ret_code})')

  time.sleep(sync_wait_sec)
  return stdout.strip()


def take_screenshot(
    ad: typing_utils.AdbDevice, host_destination: str,
    file_name: str | None = None
) -> str:
  """Takes a screenshot of the device.

  Args:
    ad: Adb like device.
    host_destination: Full path to the directory to save in the host.
    file_name: Desired file name for the screenshot. If not  provided, a
      timestamp-based name (e.g., 'screenshot_2023-11-23_15-30-12.png') will be
      generated.

  Returns:
    Full path to the saved screenshot file on the host machine.
  """
  if file_name is None:
    time_stamp_string = utils.get_current_human_time().strip()
    time_stamp_string = (
        time_stamp_string.replace(" ", "_").replace(":", "-"))
    file_name = f"screenshot_{time_stamp_string}.png"

  device_path = os.path.join("/storage/emulated/0/", file_name)
  ad.adb.shell(shlex.split(f"screencap -p {device_path}"))
  os.makedirs(host_destination, exist_ok=True)
  screenshot_path = os.path.join(host_destination, file_name)
  ad.adb.pull(shlex.split(f"{device_path} {screenshot_path}"))
  ad.log.info("Screenshot taken at %s", screenshot_path)
  ad.adb.shell(shlex.split(f"rm {device_path}"))
  return screenshot_path
