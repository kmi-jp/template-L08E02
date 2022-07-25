# L08E02: Data 4
V balíčku `data` upravte metody `DataFrame.from_csv(filepath, separator=",")` a `Series.from_csv(filepath, separator=",")` tak, aby namísto textu přijímaly instanci třídy `pathlib.Path` pomoci parametru `filepath` (tedy soubor s příponou `csv`).

```python
import pathlib
from data.dataframe import DataFrame

df = DataFrame.from_csv(filepath=pathlib.Path.cwd() / "input.csv")
```

## Lokální testování
Funkčnost řešení ověříte následujícím příkazem:

```bash
pytest
```