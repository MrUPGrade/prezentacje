import pytest


@pytest.fixture(scope='module')
#@pytest.fixture
def initial_dict(request):
    def finalizer():
        print('## finish ##', end='')

    request.addfinalizer(finalizer)

    return {'1': 1, '2': 2}


def test_fixture_1(initial_dict):
    assert '1' in initial_dict


def test_fixture_2(initial_dict):
    assert '2' in initial_dict
