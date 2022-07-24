import pytest

from data.series import Series


@pytest.fixture
def users_data():
    return ["user 1", "user 2", "user 3", "user 4"]


def test_from_csv(users_data, tmp_path):
    input_text = """user 1,user 2,user 3,user 4
Lukas Novak,Petr Pavel,Pavel Petr,Ludek Skocil
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(input_text)

    data = Series.from_csv(filepath=csv_file, separator=",")

    assert data.index.labels == users_data
    assert list(data.values) == list(
        ["Lukas Novak", "Petr Pavel", "Pavel Petr", "Ludek Skocil"]
    )
