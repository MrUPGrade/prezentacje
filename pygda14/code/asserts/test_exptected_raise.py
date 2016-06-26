import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as ex_info:
        1 / 0
