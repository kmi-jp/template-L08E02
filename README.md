# L08E02: Data 4
V balíčku `data` upravte metody `DataFrame.from_csv()` a `Series.from_csv()` tak, aby namísto textu přijímaly instanci třídy `pathlib.Path` (tedy soubor s příponou `csv`).

```python
import pathlib
from data.dataframe import DataFrame

df = DataFrame.from_csv(pathlib.Path.cwd() / "input.csv")
```