import types
import pytest

from data.dataframe import DataFrame
from data.index import Index
from data.series import Series


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


def test_iteratiron(names, salaries, cash_flow, columns):
    data = DataFrame([names, salaries, cash_flow], columns=columns)

    assert isinstance(data.__iter__(), types.GeneratorType)
    assert list(data) == columns.labels


def test_items(names, salaries, cash_flow, columns):
    data = DataFrame([names, salaries, cash_flow], columns=columns)

    assert isinstance(data.items(), zip)

    test_columns = []
    test_values = []

    for column, value in data.items():
        test_columns.append(column)
        test_values.append(value)

    assert test_columns == columns.labels
    assert test_values == [names, salaries, cash_flow]


def test_index(names, salaries, cash_flow, columns):
    data = DataFrame([names, salaries, cash_flow], columns=columns)

    assert data.index == names.index


@pytest.mark.parametrize(
    "function",
    [DataFrame, DataFrame.from_csv, DataFrame.get, DataFrame.shape, DataFrame.index],
)
def test_docstrings(function):
    assert function.__doc__ is not None