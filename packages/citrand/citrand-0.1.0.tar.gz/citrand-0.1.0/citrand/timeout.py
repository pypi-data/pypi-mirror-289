# This file is part of Citrand.
# Copyright (C) 2024 Taylor Rodríguez.
#
# Citrand is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Citrand is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Citrand. If not, see <https://www.gnu.org/licenses/>.

"""
Simple API to enforce time limits for functions.

Typical usage:
```python
from citrand import timeout

@timeout.timeout(minutes=1)
def function():
    "This function should run in under one minute."
```
"""

import contextlib
import functools
import signal
import types
from typing import Any, Callable, Generator, NoReturn

__all__ = ["timeout_context", "timeout"]


@contextlib.contextmanager
def timeout_context(
    seconds: int = 0, minutes: int = 0, hours: int = 0
) -> Generator[None, Any, None]:
    """Raise `TimeoutError` if a synchronous function runs for too long."""
    seconds_per_minute = 60
    seconds_per_hour = seconds_per_minute**2

    # Calculate the total number of seconds to wait for.
    timeout_seconds = (
        seconds + minutes * seconds_per_minute + hours * seconds_per_hour
    )

    def signal_handler(signum: int, frame: types.FrameType | None) -> NoReturn:
        """Handle the signal by raising a `TimeoutError`."""
        message = "Timed out after "
        hours = timeout_seconds // seconds_per_hour
        minutes = (timeout_seconds % seconds_per_hour) // seconds_per_minute
        seconds = (timeout_seconds % seconds_per_hour) % seconds_per_minute

        if hours:
            message += f" {hours}h"

        if minutes:
            message += f" {minutes}m"

        message += f" {seconds}s"

        raise TimeoutError(message)

    # Create an alarm that will raise an Exception after `timeout_seconds` sec.
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(timeout_seconds)

    try:
        yield
    finally:
        signal.alarm(0)


def timeout(
    seconds: int = 0, minutes: int = 0, hours: int = 0
) -> Callable[..., Callable[..., Any]]:
    """Raise `TimeoutError` if a synchronous function runs for too long."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with timeout_context(seconds, minutes, hours):
                return func(*args, **kwargs)

        return wrapper

    return decorator
