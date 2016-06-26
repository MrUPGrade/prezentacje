import pytest


@pytest.mark.parametrize('x,y,expected',[
    (1, 1, 2),
    (2, 3, 4)
])
def test_simple_add(x, y, expected):
    result = x + y
    assert result == expected