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

"""Utilities used by ui_pages module."""
import abc
import re

from typing import Any, Callable, Dict


class TextMatchStrategy(abc.ABC):
  """Strategy to match text."""

  @abc.abstractmethod
  def match(self, text: str) -> bool:
    """Matches input text.

    Args:
      text: The text to match.

    Returns:
      True iff the input text is wanted.
    """
    raise NotImplementedError


class PlainTextMatchStrategy(TextMatchStrategy):
  """Strategy to match by plain text.

  Attributes:
    expected_text: Text to match.
  """

  def __init__(self, expected_text: str):
    self.expected_text = expected_text

  def match(self, text: str) -> bool:
    return self.expected_text == text


class RETextMatchStrategy(TextMatchStrategy):
  """Strategy to match by regular expression.

  Attributes:
    pattern_object: Regular expression to search text.
  """

  def __init__(self, text_re: str):
    self.pattern_object = re.compile(text_re)

  def match(self, text: str) -> bool:
    return self.pattern_object.search(text) is not None


def dr_wakeup_before_op(op: Callable[..., Any]) -> Callable[..., Any]:
  """Sends keycode 'KEYCODE_WAKEUP' before conducting UI function.

  Args:
    op: UI function (click, swipe etc.)

  Returns:
    Wrapped UI function.
  """
  def _wrapper(*args: Any, **kargs: Dict[str, Any]) -> Callable[..., Any]:
    """Wrapper of UI function.

    Args:
      *args: Argument list passed into UI function.
      **kargs: key/value argument passed into UI function.

    Returns:
      The returned result by calling the wrapped UI operation method.
    """

    ui_page_self = args[0]
    ui_page_self.ad.adb.shell(
        'input keyevent KEYCODE_WAKEUP')
    return op(*args, **kargs)

  return _wrapper
