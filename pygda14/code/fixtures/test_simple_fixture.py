import pytest


@pytest.fixture
def initial_dict():
    return {'1': 1}


def test_fixture_1(initial_dict2):
    initial_dict['2'] = 2

    assert '2' in initial_dict
    assert '1' in initial_dict
