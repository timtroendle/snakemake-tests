from pathlib import Path

import pandas as pd

PATH_TO_DATA = Path("some-data.csv")


def test_last_entry_not_above_1():
    data = pd.read_csv(PATH_TO_DATA)
    assert data.iloc[-1, 0] <= 1
