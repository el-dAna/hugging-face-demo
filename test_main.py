import pytest
from functions import add, subtract


@pytest.mark.parametrize("value", [[5, 6, 11], [-5, 6, 1], [0, 0, 0], [-5, 0, -5]])
def test_add(value):
    a, b, result = value
    assert add(a, b) == result


@pytest.mark.parametrize("value", [[5, 6, -1], [-5, 6, -11], [0, 0, 0], [-5, 0, -5]])
def test_subtract(value):
    a, b, result = value
    assert subtract(a, b) == result
