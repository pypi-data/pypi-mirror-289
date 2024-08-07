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


from dataclasses import fields
from typing import Sequence
from bttc import bt_data
from bttc import constants
from bttc import general_data
from bttc import errors
from bttc import ble_data
import logging
import re


BondedDeviceInfo = bt_data.BondedDeviceInfo
LeAudioServiceInfo = ble_data.LeAudioService
ActiveGroupInfo = ble_data.ActiveGroupInfo
GroupInfo = ble_data.GroupInfo
DeviceInfo = ble_data.DeviceInfo
StateMachineLog = ble_data.StateMachineLog
LeAudioStateMachine = ble_data.LeAudioStateMachine


def parse_audio_dump_for_volume_info(
    log_content: str) -> dict[str, general_data.AudioStreamVolume]:
  """Parses the audio dumps to retrieve the volume information.

  `log_content` is expected to collect from below command in DUT:
  ```
  $ dumpsys audio
  ...
  Stream volumes (device: index)
  - STREAM_VOICE_CALL:
    Muted: false
    Muted Internally: false
    Min: 1
    Max: 7
    streamVolume:5
    Current: 1 (earpiece): 4, 10 (bt_sco): 5, 80 (bt_a2dp): 5, ...(default): 5
    Devices: bt_a2dp(80)
    Volume Group: AUDIO_STREAM_VOICE_CALL
  ...
  ```

  Args:
    log_content: Log content to parse.

  Returns:
    dict object with key as name of audo stream and value as corresponding
    parsing result.

  Raises:
    ValueError: Unexpected log content.
  """
  stream_header_pattern = re.compile('STREAM_([_A-Z0-9]+)')
  log_lines = log_content.split('\n')
  current_volume_setting_record: general_data.AudioStreamVolume | None = None
  collected_volume_info: dict[str, general_data.AudioStreamVolume] = {}
  is_parse_done = False
  for i, line in enumerate(log_lines):
    if line.startswith('Stream volumes'):
      # Start parsing
      for line in log_lines[i+1:]:
        line = line.strip()
        if line.startswith('- '):
          # New volume type. e.g.:
          # - STREAM_VOICE_CALL:
          #   Muted: false
          #   Muted Internally: false
          #   Min: 1
          #   Max: 7
          #   streamVolume:5
          #   Current: 1 (earpiece): 5, 80 (bt_a2dp): 5, 40000000 (default): 5
          #   Devices: earpiece(1)
          #   Volume Group: AUDIO_STREAM_VOICE_CALL
          mth = stream_header_pattern.search(line)
          if not mth:
            raise ValueError(f'Unknown stream header title: {line}')
          current_volume_setting_record = (
              general_data.AudioStreamVolume(name=mth.group(1)))
        elif line.startswith('Muted:'):
          current_volume_setting_record.is_muted = (
              False if line.split(':')[1].strip() == 'false' else True)
        elif line.startswith('Min:'):
          try:
            current_volume_setting_record.min_level = (
                int(line.split(':')[1].strip().split()[0]))
          except ValueError as ex:
            logging.warning(
                f'Unknown Min setting="{line}"! Use default 0 instead: {ex}')
            current_volume_setting_record.min_level = 0
        elif line.startswith('Max:'):
          current_volume_setting_record.max_level = (
              int(line.split(':')[1].strip()))
        elif line.startswith('streamVolume:'):
          current_volume_setting_record.stream_volume_level = (
              int(line.split(':')[1].strip()))
        elif line.startswith('Devices:'):
          current_volume_setting_record.devices = line.split(':')[1].strip()
        elif line.startswith('Current:'):
          current_volume_setting_record.current = (
              int(line.split(':')[1].strip().split()[0]))
        elif line == '':
          if current_volume_setting_record is None:
            is_parse_done = True
            break

          # Save the parsing record
          collected_volume_info[current_volume_setting_record.name] = (
              current_volume_setting_record)
          current_volume_setting_record = None

      if is_parse_done:
        break

  if not is_parse_done:
    raise ValueError('Audio stream content is not found!')

  return collected_volume_info


def parse_bluetooth_crash_info(log_content: str) -> Sequence[str]:
  """Parses the BT manager log to collect crash information.

  For this function to work, we expect below log snippet from given log content:

  ===
  Bluetooth crashed 2 times
  12-17 10:23:00
  12-17 11:29:13
  ===

  If there is no crash, log will look like:
  ===
  Bluetooth crashed 0 times
  ===

  Args:
    log_content: The dumped BT manager log.

  Returns:
    Sequence of crash time string in format '%m-%d %H:%M:%S'.

  Raises:
    errors.LogParseError:
      Fail to parse the log. It doesn't contain the key words.
  """
  lines = log_content.split('\n')
  for line_num, line in enumerate(lines):
    match_object = re.search(
      r'Bluetooth crashed (?P<crash_time>\d+) time', line)
    if match_object is None:
      continue

    crash_time = int(match_object.group('crash_time'))
    if crash_time > 0:
      begin_crash_time_num = line_num + 1
      return [
          line.strip()
          for line in lines[begin_crash_time_num:begin_crash_time_num +
                            crash_time]
      ]
    return []

  raise errors.LogParseError(log_content)


def parse_bonded_device_info(log_content: str) -> list[BondedDeviceInfo]:
  """Parses the BT manager log to collect bonded device information.

  For this function to work, we expect below log snippet from given log content:

  ===
  Bonded devices:
    28:6F:40:57:AC:44 [ DUAL ] JBL TOUR ONE M2
    CC:98:8B:C0:F2:B8 [ DUAL ] WH-1000XM3
  ===
  Or
  ===
    Bonded devices:
    7C:96:D2:87:44:75 [ DUAL ][ 0x240418 ] Acrux
  ===

  If there is no bonded device, log will look like:
  ===
  Bonded devices:

  ===

  Then this method will also parse profile `HeadsetService`:
  ===
  Profile: HeadsetService
    mMaxHeadsetConnections: 5
    ...
    ==== StateMachine for XX:XX:XX:XX:F1:BF ====
      mCurrentDevice: XX:XX:XX:XX:F1:BF
      mCurrentState: Connected
      mPrevState: Connecting
      ...
  ===
  to search the connection states of bonded devices.

  Args:
    log_content: The dumped BT manager log.

  Returns:
    List[BondedDevice] : Dataclass of BondedDevice.
      Ex:
        [BondedDevice(mac_address='74:45:CE:F2:0F:EA',
                      device_name='WI-XB400',
                      device_type='DUAL')]
  Raises:
    errors.LogParseError:
      Fail to parse the log. It doesn't contain the key words.
  """
  if re.search(r'Bonded devices:\n', log_content) is not None:
    mac_2_bonded_info = {}
    output = re.finditer(
      r'(?P<mac_address>\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})'
      r'\s\[\s+(?P<device_type>.*?)\s+\](\[.*\])?'
      r'\s(?P<device_name>.*?)\n',
      log_content,
    )
    bonded_devices = []
    for device in output:
      mac_address = device.group('mac_address')
      device_type = constants.BluetoothDeviceType.from_str(
          device.group('device_type'))
      device_name = device.group('device_name')
      bonded_device_info = BondedDeviceInfo(
          mac_addr=mac_address,
          name=device_name,
          bt_type=device_type)
      bonded_devices.append(bonded_device_info)
      mac_2_bonded_info[mac_address[-5:]] = bonded_device_info

    # Search `Profile: HeadsetService`
    start_profile_headset_service = False
    start_profile_headset_service_state_machine_mac = None
    for line in log_content.split('\n'):
      if line.strip() == 'Profile: HeadsetService':
        start_profile_headset_service = True

      if start_profile_headset_service:
        matcher = re.search(
            '==== StateMachine for XX:XX:XX:XX:(.*) ====', line)
        if matcher:
          start_profile_headset_service_state_machine_mac = matcher.group(1)

      if start_profile_headset_service_state_machine_mac:
        if not line:
          start_profile_headset_service = False
          start_profile_headset_service_state_machine_mac = None
        elif line.strip().startswith('mCurrentState:'):
          bonded_device_info = (
              mac_2_bonded_info[
                  start_profile_headset_service_state_machine_mac])
          bonded_device_info.connect_state = line.split(':')[1].strip()

    return bonded_devices

  raise errors.LogParseError(log_content)


def get_ident_level(line: str) -> int:
  """Calculate the tab size of text.

  Args:
      line (str): Content per line

  Returns:
      int: size of the tab
  """
  return len(line) - len(line.lstrip())


def set_dataclass_attr(data_class_obj, k, v) -> None:
  """Set attribute for a dataclass"""
  field_names = [f.name for f in fields(data_class_obj)]
  if k in field_names:
    setattr(data_class_obj, k, v)
  else:
    data_class_obj.others[k] = v


def get_section_object(parent_section: object, sub_section_name: str,
                       key: str, value: str) -> object:
  """Adding subsection to parent section, and change the pointer to subsection.

  Args:
      parent_section (object): Dataclass of the parent section
      sub_section_name (str): Title of the subsection
      key (str): key of the data
      value (str): value of the data

  Returns:
      object: dataclass of subsection
  """
  match sub_section_name:
    case "ActiveGroupsinformation":
      new_section_obj = ActiveGroupInfo()
      parent_section.active_group_list.append(new_section_obj)
      return new_section_obj
    case "Group":
      new_section_obj = GroupInfo()
      set_dataclass_attr(new_section_obj, key, value)
      parent_section.group_list.append(new_section_obj)
      return new_section_obj
    case "mDevice":
      new_section_obj = DeviceInfo()
      set_dataclass_attr(new_section_obj, key, value)
      parent_section.device_list.append(new_section_obj)
      return new_section_obj
    case "StateMachineLog":
      new_section_obj = StateMachineLog()
      parent_section.state_machine_list.append(new_section_obj)
      return new_section_obj
    case "LeAudioStateMachine":
      new_section_obj = LeAudioStateMachine()
      parent_section.le_audio_state_machine_list.append(new_section_obj)
      return new_section_obj


def parse_le_audio_service_info(log_content: str) -> LeAudioServiceInfo:
  """Parses the BT manager log to collect LE audio service information.

  For this function to work, we expect below log snippet from given log content:

  ===
  Profile: LeAudioService
    isDualModeAudioEnabled: false
    Active Groups information:
      currentlyActiveGroupId: 1
      mActiveAudioOutDevice: XX:XX:XX:XX:38:31
  ===

  If there is no LE audio service, log will look like:
  ===
  Profile: LeAudioService
    isDualModeAudioEnabled: false
    Active Groups information:
      currentlyActiveGroupId: -1
      mActiveAudioOutDevice: null

  ===

  Args:
    log_content: The dumped BT manager log.

  Returns:
    LeAudioServiceInfo : Dataclass of LeAudioService.

  Raises:
    errors.LogParseError:
      Fail to parse the log. It doesn't contain the key words.
  """
  stack = []
  key = value = None
  current_ident_level = 2
  root_sect_obj = cur_sect_obj = LeAudioServiceInfo()
  previous_key = None
  if "Profile: LeAudioService" in log_content:
    for part_content in log_content.split("\n\n"):
      if "Profile: LeAudioService" not in part_content:
        continue
      for line in part_content.split("\n")[1:]:
        ident_level = get_ident_level(line)
        if ident_level == 2 and type(cur_sect_obj) not in [
            LeAudioServiceInfo, ActiveGroupInfo, GroupInfo, DeviceInfo, ]:
          cur_sect_obj, current_ident_level = stack.pop()
        line = re.sub(r'\s', '', line)

        if not line:
          continue

        if ident_level > current_ident_level:
          new_sect_obj = get_section_object(
            cur_sect_obj, previous_key, key, value)
          del cur_sect_obj.others[previous_key]
          stack.append((cur_sect_obj, current_ident_level))
          current_ident_level = ident_level
          cur_sect_obj = new_sect_obj

        elif current_ident_level > ident_level:
          cur_sect_obj, current_ident_level = stack.pop()

        first_mark = line.find("=") if line.find(":") < 0 else line.find(":")
        key = line[:first_mark]
        value = line[first_mark+1:]

        set_dataclass_attr(cur_sect_obj, key, value)
        previous_key = key

    return root_sect_obj

  raise errors.LogParseError(log_content)
