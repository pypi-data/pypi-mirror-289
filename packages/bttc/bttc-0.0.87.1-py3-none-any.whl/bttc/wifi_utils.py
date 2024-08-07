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

"""Utility to support common WiFi operations/methods.

TODO(johnkclee): Add unit test cases.
"""
from __future__ import annotations

import enum
import logging
import shlex
import time

import bttc
from bttc import common_data
from bttc import core
from bttc import errors
from bttc.utils import device_factory

from mobly.controllers import android_device

import re
from typing import TypeAlias, Union


BINDING_KEYWORD = 'wifi'
ANDROID_DEVICE: TypeAlias = android_device.AndroidDevice


class WiFiModule(core.UtilBase):
  """WiFi module to hold WiFi related functions define in this module."""

  NAME = BINDING_KEYWORD
  DESCRIPTION = 'Utility to support WiFi operations. e.g. Get SSID name.'

  def __init__(self, ad: ANDROID_DEVICE):
    self._ad = ad
    self._bind(get_status, 'get_status')
    self._bind(start_scan, 'scan')

  @property
  def ssid_name(self) -> str:
    """The SSID (name) of the currently connected WiFi network."""
    return get_ssid_name(self._ad)

  @property
  def status(self) -> str:
    """Current WiFi status of the Android device."""
    return self.get_status()

  def is_enabled(self) -> bool:
    return self.status == WifiStatus.ENABLED

  def enable(self):
    """Enables Wifi."""
    self.ad.adb.shell(['svc', 'wifi', 'enable'])

  def disable(self):
    """Disables Wifi."""
    self.ad.adb.shell(['svc', 'wifi', 'disable'])

  def login(self, ssid_name: str, password: str) -> bool:
    """Logins WiFi."""
    if ssid_name == self.ssid_name:
      logging.info('Already login WiFi with SSID name="%s"', ssid_name)
      return True

    std, _, return_code = bttc.safe_adb_shell(self.ad)(
        f'cmd wifi connect-network {shlex.quote(ssid_name)} '
        f'wpa2 {shlex.quote(password)}')

    if return_code != 0:
      raise errors.AdbExecutionError(return_code, std)

    logging.info(std)
    return self.ssid_name == ssid_name


def bind(
    ad: Union[ANDROID_DEVICE, str],
    init_mbs: bool = False, init_sl4a: bool = False,
    init_snippet_uiautomator: bool = False) -> ANDROID_DEVICE:
  """Binds the input device with functions defined in current module.

  Sample Usage:
  ```python
  >>> from bttc import wifi_utils
  >>> dut = wifi_utils.bind('35121FDJG0005P')
  >>> dut.wifi.status()
  <WifiStatus.ENABLED: 'enabled'>
  >>> dut.wifi.ssid_name
  'Pixel_5413'
  >>> dut.wifi.scan()  # Start WiFi scan
  ```

  Args:
    ad: If string is given, it stands for serial of device. Otherwise, it should
        be the Android device object.

  Returns:
    The device with binded functions defined in current module.
  """
  device = device_factory.get(
      ad, init_mbs=init_mbs, init_sl4a=init_sl4a,
      init_snippet_uiautomator=init_snippet_uiautomator)
  device.load_config({BINDING_KEYWORD: WiFiModule(device)})
  return device


class WifiStatus(common_data.StrEnum):
  ENABLED = 'enabled'
  DISABLED = 'disabled'

  @classmethod
  def from_str(cls, input_str: str) -> WifiStatus:
    """Gets Wifi status enum from string."""
    for wifi_status_enum in cls:
      if wifi_status_enum == input_str.strip():
        return wifi_status_enum

    raise errors.UnknownWiFiStatusError(input_str)


class WifiSSIDStatus(enum.Enum):
  ASSOCIATING = 'ASSOCIATING'
  SCANNING = 'SCANNING'
  DISCONNECTED = 'DISCONNECTED'
  READY = 'READY'

  @classmethod
  def from_str(cls, adb_output: str) -> tuple[WifiSSIDStatus, str]:
    if 'wpa_state=SCANNING' in adb_output:
      return (cls.SCANNING, '')
    if 'wpa_state=DISCONNECTED' in adb_output:
      return (cls.DISCONNECTED, '')
    if 'wpa_state=ASSOCIATING' in adb_output:
      return (cls.ASSOCIATING, '')

    matcher = re.search(r'^ssid\s*=\s*(.*)', adb_output, re.M)
    if matcher:
      return (cls.READY, matcher.group(1).strip())

    raise errors.AdbUnknownOutputError(adb_output)


def get_status(ad: android_device.AndroidDevice) -> WifiStatus:
  """Retrieves the current WiFi status of the Android device.

  Args:
    ad: The Android device object.

  Returns:
    WifiStatus: An object representing the WiFi status
        (e.g., enabled, disabled).

  Raises:
    AdbExecutionError: If the command to fetch WiFi information fails.
    UnknownWiFiStatusError: If the function cannot parse a valid status from
        the command output.
  """
  std, _, return_code = bttc.safe_adb_shell(ad)('dumpsys wifi')

  if return_code != 0:
    raise errors.AdbExecutionError(return_code, std)

  # e.g.: Wi-Fi is disabled
  matcher = re.search('Wi-Fi is (.*)', std)
  if matcher:
    return WifiStatus.from_str(matcher.group(1).strip())
  else:
    raise errors.UnknownWiFiStatusError(std)


def get_ssid_name(ad: android_device.AndroidDevice) -> str | None:
  """Retrieves the SSID (name) of the currently connected WiFi network.

  Args:
    ad: The Android device object.

  Returns:
    str: The SSID name, or None if no network is connected.

  Raises:
    AdbExecutionError: If the command to fetch WiFi status fails. Includes
        return code, output, and a message suggesting to check WiFi status.
    AdbUnknownOutputError: If the function cannot parse a valid SSID from
        the command output.
  """
  for retry in range(1, 20):
    std, _, return_code = bttc.safe_adb_shell(ad)(
        'wpa_cli -iwlan0 -g@android:wpa_wlan0 IFNAME=wlan0 status ')

    if return_code != 0:
      raise errors.AdbExecutionError(
          return_code, std, guiding_msg='Check if Wifi is enabled!')

    ssid_status, ssid_name = WifiSSIDStatus.from_str(std)

    if ssid_status in {WifiSSIDStatus.ASSOCIATING, WifiSSIDStatus.SCANNING}:
      logging.warning('WiFi is under scanning...retry=%s', retry)
      time.sleep(1)
      continue

    break

  # e.g.: ssid=Pixel_5413
  if ssid_status == WifiSSIDStatus.READY:
    return ssid_name
  else:
    logging.warning('Wifi SSID is not ready (%s)!', ssid_status)
    return ''


def start_scan(ad: android_device.AndroidDevice):
  """Initiates a WiFi scan on the Android device.

  Args:
    ad: The Android device object.

  Raises:
    AdbExecutionError: If the scan command fails to execute successfully.
        The error includes the return code and command output.
  """
  std, _, return_code = bttc.safe_adb_shell(ad)(
      'cmd wifi start-scan')

  if return_code != 0:
    raise errors.AdbExecutionError(return_code, std)
