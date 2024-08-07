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

"""Utility to handle the key events of Android like device."""

from __future__ import annotations

import enum
import shlex
from typing import Optional

from mobly.controllers.android_device_lib import adb

from bttc.utils import retry
from bttc.utils import typing_utils


@enum.unique
class MediaKeyCode(enum.Enum):
  """Media key codes."""
  NEXT = 87
  PREVIOUS = 88
  PLAY = 126
  PAUSE = 127


@enum.unique
class VolumeKeyCode(enum.Enum):
  """Volume related key codes."""
  # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_VOLUME_DOWN
  DOWN = 25

  # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_VOLUME_MUTE
  MUTE = 164

  # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_VOLUME_UP
  UP = 24


@enum.unique
class KeycodeNumPad(enum.Enum):
  """Enum class for Numpad key event."""

  NUM_0 = '0'
  NUM_1 = '1'
  NUM_2 = '2'
  NUM_3 = '3'
  NUM_4 = '4'
  NUM_5 = '5'
  NUM_6 = '6'
  NUM_7 = '7'
  NUM_8 = '8'
  NUM_9 = '9'
  ADD = 'ADD'
  COMMA = 'COMMA'
  DIVIDE = 'DIVIDE'
  DOT = 'DOT'
  EQUALS = 'EQUALS'
  LEFT_PAREN = 'LEFT_PAREN'
  MULTIPLY = 'MULTIPLY'
  RIGHT_PAREN = 'RIGHT_PAREN'
  SUBTRACT = 'SUBTRACT'

  @classmethod
  def from_str(cls, label: str) -> Optional[KeycodeNumPad]:
    for kc_enum in cls:
      if kc_enum.value == label:
        return kc_enum

    return None

  @property
  def key(self) -> str:
    if self.name.startswith('NUM'):
      return self.name[4:]

    return self.name


class KeyEventHandler:
  """Class to handle the key events of Android adb device.

  For all supported key event, refer to go/android_key_events
  """

  def __init__(self, device: typing_utils.AdbDevice):
    self._device = device

  @retry.retry_on_exception(
      retry_value=adb.Error,
      retry_intervals=retry.FuzzedExponentialIntervals(
          initial_delay_sec=1,
          num_retries=5,
          factor=1.1))
  def send_keycode(self, keycode: str | int):
    """Sends key event.

    Args:
      keycode: Key event code.
    """
    if isinstance(keycode, str):
      self._device.adb.shell(shlex.split(
          f'input keyevent KEYCODE_{keycode}'))
    else:
      self._device.adb.shell(shlex.split(
          f'input keyevent {keycode}'))

  def key_media_next(self):
    """Sends key event MEDIA_NEXT."""
    self.send_keycode(MediaKeyCode.NEXT.value)

  def key_media_play(self):
    """Sends key event MEDIA_PLAY."""
    self.send_keycode('MEDIA_PLAY')

  def key_media_pause(self):
    """Sends key event MEDIA_PAUSE."""
    self.send_keycode('MEDIA_PAUSE')

  def key_media_play_pause(self):
    """Sends key event MEDIA_PLAY_PAUSE."""
    self.send_keycode('MEDIA_PLAY_PAUSE')

  def key_media_previous(self):
    """Sends key event MEDIA_PREVIOUS."""
    self.send_keycode(MediaKeyCode.PREVIOUS.value)

  def key_power(self):
    """Sends key event POWER.

    For details, please refer to go/android_keyevent_power
    """
    self.send_keycode('POWER')

  def key_sleep(self):
    """Sends key event SLEEP.

    For details, please refer to go/android_keyevent_sleep
    """
    self.send_keycode('SLEEP')

  def key_wakeup(self):
    """Sends key event WAKEUP.

    For details, please refer to go/android_keyevent_wakeup
    """
    self.send_keycode('WAKEUP')

  def key_menu(self):
    """Sends key event MENU.

    For details, please refer to go/android_keyevent_menu
    """
    self.send_keycode('MENU')

  def key_del(self):
    """Sends key event DEL.

    For details, please refer to go/android_keyevent_del
    """
    self.send_keycode('DEL')

  def key_enter(self):
    """Sends key event ENTER.

    For details, please refer to go/android_keyevent_enter
    """
    self.send_keycode('ENTER')

  def key_escape(self):
    """Sends key event ESCAPE."""
    self.send_keycode('ESCAPE')

  def key_back(self):
    """Sends key event BACK.

    For details, please refer to go/android_keyevent_back
    """
    self.send_keycode('BACK')

  def key_home(self):
    """Sends key event HOME.

    For details, please refer to go/android_keyevent_home
    """
    self.send_keycode('HOME')

  def key_call(self):
    """Sends key event CALL.

    For details, please refer to go/android_keyevent_call
    """
    self.send_keycode('CALL')

  def key_endcall(self):
    """Sends key event ENDCALL.

    For details, please refer to go/android_keyevent_endcall
    """
    self.send_keycode('ENDCALL')

  def key_numpad(self, enum_numpad: KeycodeNumPad):
    """Sends key event as numpad.

    Args:
      enum_numpad: Numpad key event enum.
    """
    self.send_keycode(f'NUMPAD_{enum_numpad.key}')

  def key_numpad_by_st(self, numpad_str: str):
    """Sends numpad key event.

    Args:
      numpad_str: Numpad as string.
    """
    enum_numpad = KeycodeNumPad.from_str(numpad_str)
    if enum_numpad is None:
      raise ValueError(f'Invalid numpad string="{numpad_str}"')

    self.key_numpad(enum_numpad)

  def key_volume_down(self):
    """Sends key event `KEYCODE_VOLUME_DOWN`."""
    self.send_keycode(VolumeKeyCode.DOWN.value)

  def key_volume_mute(self):
    """Sends key event `KEYCODE_VOLUME_MUTE`."""
    self.send_keycode(VolumeKeyCode.MUTE.value)

  def key_volume_up(self):
    """Sends key event `KEYCODE_VOLUME_UP`."""
    self.send_keycode(VolumeKeyCode.UP.value)
