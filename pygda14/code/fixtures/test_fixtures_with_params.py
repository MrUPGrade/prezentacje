import pytest


@pytest.fixture(params=[' ', '\t'])
def input_context(request):
    return request.param + 'a'


def super_strip(input_str):
    """To jest nasza super funkcja !"""
    return input_str.strip()


def test_fixture_1(input_context):
    result = super_strip(input_context)

    assert result == 'a'
