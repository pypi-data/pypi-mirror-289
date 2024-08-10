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

"""HFP Facade module."""

from __future__ import annotations

import abc
import dataclasses
from typing import Protocol

from bttc.profiles.hfp import constants
from bttc.profiles.hfp import hfp_data
from bttc.utils import typing_utils


_CALL_IDLE = hfp_data.CallStateEnum.IDLE


class DialerSimulator(Protocol):
  """Abstract class for dialer simulator behaviors."""

  def incoming_call(self) -> CallResult:
    """Simulates incoming call.

    This method is only valid with dialer simulator available in DUT.
    For details, please refer to go/dialer-simulator

    Returns:
      dataclass CallResult to represent calling result.
    """
    ...

  def outgoing_call(self) -> CallResult:
    """Simulates outgoing call.

    This method is only valid with dialer simulator available in DUT.
    For details, please refer to go/dialer-simulator

    Returns:
      dataclass CallResult to represent calling result.
    """
    ...


class PhoneDevice(abc.ABC):
  """Abstract phone device for HFP testing.

  Attributes:
    phone_number: Phone number of device.
    log: Logger object.
  """

  def __init__(self, phone_number: str, log: typing_utils.LogProtocol):
    self.phone_number = phone_number
    self.log = log

  @property
  def call_state(self) -> hfp_data.CallStateEnum:
    return self.get_call_state()

  def is_incall(self) -> bool:
    """Checks if the device is in call or not.

    Returns
      True iff the device is in call.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `is_incall`!')

  def get_call_state(self) -> hfp_data.CallStateEnum:
    """Gets the call state of device.

    Returns:
      The call state.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `get_call_state`!')

  def wait_for_call_state(self,
                          state: hfp_data.CallStateEnum,
                          timeout_sec: int = 30,
                          wait_interval: int = 3) -> bool:
    """Waits for specific call state.

    Args:
      state: Call state to wait for.
      timeout_sec: Timeout in second to wait for the target call state.
      wait_interval: Number of second to wait in each cycle.

    Returns:
      True if the device reaches the target call state.

    Raises:
      BrokenPipeError: If called while the socket is disconnected.
      jsonrpc_client_base.Error: Something wrong with SL4A API call.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `wait_for_call_state`!')

  def incoming_call(self) -> CallResult:
    """Simulates incoming call.

    This method is only valid with dialer simulator available in DUT.

    Returns:
      dataclass CallResult to represent calling result.
    """
    raise NotImplementedError('`incoming_call` is not implemented!')

  def outgoing_call(self) -> CallResult:
    """Simulates outgoing call.

    This method is only valid with dialer simulator available in DUT.

    Returns:
      dataclass CallResult to represent calling result.
    """
    raise NotImplementedError('`outgoing_call` is not implemented!')

  def call(self, callee: PhoneDevice) -> CallResult:
    """Calls the target device.

    Args:
      callee: The target device to call.

    Returns:
      dataclass CallResult to represent calling result.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `call`!')

  def end_call(self) -> bool:
    """Ends the call.

    Returns:
      True iff the device can reach call state as IDLE.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `end_call`!')

  def answer_call(self) -> bool:
    """Answers the call.

    Returns:
      True iff the device answers call successfully.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `answer_call`!')

  def reject_call(self) -> bool:
    """Rejects the call.

    Returns:
      True iff the device rejects call successfully.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `reject_call`!')

  def mute_call(self) -> bool:
    """Mutes the call.

    Returns:
      True iff the device rejects call successfully.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `mute_call`!')

  def set_call_volume(self, volume: int):
    """Sets volume of call."""
    raise NotImplementedError(
        f'Subclass={self} should implement `set_call_volume`!')

  def set_call_audio_route(self, audio_route: constants.AudioRoute):
    """Sets call audio route.

    Args:
      audio_route: Audio route to switch to.
    """
    raise NotImplementedError(
        f'Subclass={self} should implement `set_call_audio_route`!')

  def set_call_audio_route_to_earpiece(self):
    """Sets call audio route to earpiece."""
    self.set_call_audio_route(constants.AudioRoute.EARPIECE)


class PhoneLikeDevice(Protocol):
  """Protocl to turn device into PhoneDevice."""

  def to_phone_device(self) -> PhoneDevice:
    """Translates into phone device.

    Returns:
      Phone device.
    """
    ...


@dataclasses.dataclass
class CallResult:
  """Result of a call between two devices."""
  caller: PhoneDevice
  callee: PhoneDevice
  error: str | None = None


class HFPFacade:
  """HFP Facade class.

  Attributes:
    callee_device: Callee device.
    caller_device: Caller device.
  """

  def __init__(self, caller_device: PhoneDevice, callee_device: PhoneDevice):
    self._caller_device = caller_device
    self._callee_device = callee_device

  @property
  def callee_device(self) -> PhoneDevice:
    return self._callee_device

  @property
  def caller_device(self) -> PhoneDevice:
    return self._caller_device

  def make_call(
      self,
      state: hfp_data.CallStateEnum = hfp_data.CallStateEnum.ACTIVE,
  ) -> CallResult:
    """Makes a call from caller to callee to enter desired state.

    Args:
      state: The calling state to reach.

    Returns:
      dataclass CallResult to represent the calling result.
    """
    call_result = self._caller_device.call(self._callee_device)

    if state == hfp_data.CallStateEnum.ACTIVE:
        self._callee_device.answer_call()

    if not self._callee_device.wait_for_call_state(state):
      call_result.error = f'Failed to reach call state={state}'
      self._caller_device.end_call()

    return call_result

  def end_call(self) -> bool:
    """Ends the call."""
    end_call_result = self._caller_device.end_call()
    # self._callee_device.end_call()
    if any([
        not self._caller_device.wait_for_call_state(_CALL_IDLE),
        not self._callee_device.wait_for_call_state(_CALL_IDLE)]):
      end_call_result = False
      self._caller_device.log.warning(
          'Caller/Callee failed to reach call state=IDLE')

    return end_call_result
