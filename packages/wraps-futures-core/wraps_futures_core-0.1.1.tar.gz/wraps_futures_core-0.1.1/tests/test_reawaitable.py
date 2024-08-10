import pytest
from wraps_futures_core.reawaitable import wrap_reawaitable


@wrap_reawaitable
async def function() -> int:
    return 42


@pytest.mark.anyio
async def test_reawaitable() -> None:
    value = 42

    reawaitable = function()

    assert reawaitable.result.is_null()  # not cached

    assert await reawaitable == value  # executed

    assert reawaitable.result.is_some()  # cached
    assert reawaitable.result.unwrap() == value  # ... correctly

    assert await reawaitable == value  # reawaitable
