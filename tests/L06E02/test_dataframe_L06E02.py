import pytest

from data.index import Index
from data.series import Series
from data.dataframe import DataFrame


@pytest.fixture
def users():
    return Index(["user 1", "user 2", "user 3", "user 4"], name="names")


@pytest.fixture
def names(users):
    return Series(
        ["Lukas Novak", "Petr Pavel", "Pavel Petr", "Ludek Skocil"], index=users
    )


@pytest.fixture
def salaries(users):
    return Series([20000, 300000, 20000, 50000], index=users)


@pytest.fixture
def cash_flow(users):
    return Series([-100, 10000, -2000, 1100], index=users)


@pytest.fixture
def columns():
    return Index(["names", "salary", "cash flow"])


def test_str_repr(names, salaries, cash_flow, columns):
    data = DataFrame([names, salaries, cash_flow], columns=columns)

    assert str(data) == "DataFrame(4, 3)"
    assert repr(data) == "DataFrame(4, 3)"


def test_shape(names, salaries, cash_flow, columns):
    data = DataFrame([names, salaries, cash_flow], columns=columns)

    assert data.shape == (4, 3)


@pytest.mark.parametrize(
    "function",
    [DataFrame, DataFrame.from_csv, DataFrame.get, DataFrame.shape],
)
def test_docstrings(function):
    assert function.__doc__ is not None
