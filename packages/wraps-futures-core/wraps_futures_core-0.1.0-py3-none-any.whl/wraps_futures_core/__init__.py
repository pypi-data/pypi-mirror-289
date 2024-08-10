"""Core functionality of wraps-futures."""

__description__ = "Core functionality of wraps-futures."
__url__ = "https://github.com/nekitdev/wraps-futures-core"

__title__ = "wraps_futures_core"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "0.1.0"

from wraps_futures_core import typing
from wraps_futures_core.future import Future, future_value, wrap_future
from wraps_futures_core.reawaitable import ReAwaitable, wrap_reawaitable

__all__ = (
    # future
    "Future",
    "future_value",
    "wrap_future",
    # reawaitable
    "ReAwaitable",
    "wrap_reawaitable",
    # typing
    "typing",
)
