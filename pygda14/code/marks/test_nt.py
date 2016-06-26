import os
import pytest


@pytest.mark.skipif(os.name != 'nt',
                    reason='Test designed for NT system')
class TestForNT(object):
    def test_1(self):
        assert True

    def test_2(self):
        assert True
