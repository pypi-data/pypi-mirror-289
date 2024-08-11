import pytest
from wraps_core.result import Error, Ok
from wraps_futures.result import future_error, future_ok, future_result


@pytest.mark.anyio
async def test_future_result() -> None:
    value = 256
    error_value = "uwu"

    ok = Ok(value)
    error = Error(error_value)

    assert await future_ok(value) == await future_result(ok)
    assert await future_error(error_value) == await future_result(error)
