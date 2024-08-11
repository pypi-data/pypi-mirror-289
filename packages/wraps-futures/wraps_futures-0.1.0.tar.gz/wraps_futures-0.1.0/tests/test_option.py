import pytest
from wraps_core.option import NULL, Some
from wraps_futures.option import future_null, future_option, future_some


@pytest.mark.anyio
async def test_future_option() -> None:
    value = 69

    some = Some(value)
    null = NULL

    assert await future_null() == await future_option(null)
    assert await future_some(value) == await future_option(some)
