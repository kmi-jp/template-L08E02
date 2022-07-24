from data.dataframe import DataFrame


def test_from_csv(tmp_path):
    input_text = """,names,salary,cash flow
user 1,Lukas Novak,20000,-100
user 2,Petr Pavel,300000,10000
user 3,Pavel Petr,20000,-2000
user 4,Ludek Skocil,50000,1100"""

    csv_file = tmp_path / "test.csv"
    csv_file.write_text(input_text)

    data = DataFrame.from_csv(filepath=csv_file)

    assert data.columns.labels == ["names", "salary", "cash flow"]

    assert list(data.values[0].values) == list(
        ["Lukas Novak", "Petr Pavel", "Pavel Petr", "Ludek Skocil"]
    )
    assert data.values[0].index.labels == ["user 1", "user 2", "user 3", "user 4"]
    assert list(data.values[1].values) == list(map(str, [20000, 300000, 20000, 50000]))
    assert data.values[1].index.labels == ["user 1", "user 2", "user 3", "user 4"]
    assert list(data.values[2].values) == list(map(str, [-100, 10000, -2000, 1100]))
    assert data.values[2].index.labels == ["user 1", "user 2", "user 3", "user 4"]

    assert data.get("salary").apply(int).sum() == sum([20000, 300000, 20000, 50000])
