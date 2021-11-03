import types
from typing import Generator

import pytest

from data.index import Index
from data.series import Series
from data.dataframe import DataFrame


input_text=""",names,salary,cash flow
user 1,Lukas Novak,20000,-100
user 2,Petr Pavel,300000,10000
user 3,Pavel Petr,20000,-2000
user 4,Ludek Skocil,50000,1100"""

user_labels = ["user 1", "user 2", "user 3", "user 4"]
columns_labels = ["names", "salary", "cash flow"]

salaries_values = [20000, 300000, 20000, 50000]
names_values = ["Lukas Novak", "Petr Pavel", "Pavel Petr", "Ludek Skocil"]
cash_flow_values = [-100, 10000, -2000, 1100]

users = Index(user_labels, name="names")

salaries = Series(salaries_values, index=users)
names = Series(names_values, index=users)
cash_flow = Series(cash_flow_values, index=users)

columns = Index(columns_labels)
data = DataFrame([names, salaries, cash_flow], columns=columns)


def test_dataframe():
    assert data.columns == columns
    assert data.values == [names, salaries, cash_flow]
    assert isinstance(data.values, list)
    assert data.get("salary") == salaries
    assert data.get("cash flow").max() == 10000
    assert data.get("wrong key") == None


def test_iteration():
    assert isinstance(data.__iter__(), types.GeneratorType)
    assert list(data) == columns_labels


def test_items():
    assert isinstance(data.items(), zip)

    test_columns = []
    test_values = []
    for column, value in data.items():
        test_columns.append(column)
        test_values.append(value)

    assert test_columns == columns_labels
    assert test_values == [names, salaries, cash_flow]


def test_str_repr():
    assert str(data) == "DataFrame(4, 3)"
    assert repr(data) == "DataFrame(4, 3)"


def test_shape():
    assert data.shape == (4, 3)

@pytest.mark.parametrize(
    "separator",
    [
        ",",
        ";"
    ],
)
def test_from_csv(tmp_path, separator):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(input_text.replace(",", separator))

    data = DataFrame.from_csv(csv_file, separator=separator)

    assert data.columns.labels == columns_labels

    assert list(data.values[0].values) == list(names_values)
    assert data.values[0].index.labels == user_labels
    assert list(data.values[1].values) == list(map(str, salaries_values))
    assert data.values[1].index.labels == user_labels
    assert list(data.values[2].values) == list(map(str, cash_flow_values))
    assert data.values[2].index.labels == user_labels

    assert data.get("salary").apply(int).sum() == sum(salaries_values)


def test_empty_dataframe():
    with pytest.raises(ValueError):
        DataFrame([])


def test_empty_columns():
    data = DataFrame([names, salaries, cash_flow])

    assert data.columns.labels == Index(range(3)).labels
    assert data.values == [names, salaries, cash_flow]
    assert data.get(1) == salaries
    assert data.get(2).max() == 10000


@pytest.mark.parametrize(
    "function",
    [
        DataFrame,
        DataFrame.from_csv,
        DataFrame.get,
        DataFrame.shape,
        DataFrame.items
    ],
)
def test_docstrings(function):
    assert function.__doc__ is not None
