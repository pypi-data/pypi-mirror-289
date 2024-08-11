"""Various markers."""

from typing import Optional

from typing_extensions import Never

from wraps.core.panics import panic

__all__ = ("UNREACHABLE", "unreachable")

UNREACHABLE = "code marked as `unreachable` was reached"
"""The default [`unreachable`][wraps.core.markers.unreachable] panic message."""


def unreachable(message: Optional[str] = None) -> Never:
    """Marks points in code as unreachable.

    Panics with the message given. If not provided,
    [`UNREACHABLE`][wraps.core.markers.UNREACHABLE] is used.

    Arguments:
        message: The message to panic with.

    Raises:
        Panic: Always raised when calling.
    """
    if message is None:
        message = UNREACHABLE

    panic(message)
