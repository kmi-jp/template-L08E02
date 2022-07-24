import types
import pytest

from data.index import Index
from data.series import Series


@pytest.fixture
def users():
    return Index(["user 1", "user 2", "user 3", "user 4"], name="names")


@pytest.fixture
def salaries(users):
    return Series([20000, 300000, 20000, 50000], index=users)


def test_series_get_item(salaries):
    assert salaries["user 2"] == salaries.values[1]

    with pytest.raises(KeyError):
        salaries["wrong key"]


def test_iteration(salaries):
    assert isinstance(salaries.__iter__(), types.GeneratorType)
    assert sum([value for value in salaries]) == sum(salaries.values)
