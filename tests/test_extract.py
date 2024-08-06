import pytest
import pandas as pd
from src.extract import extract

def test_extract_valid_file():
    df = extract('data/raw/data.csv')
    assert isinstance(df, pd.DataFrame), "Data extraction should return a DataFrame"

def test_extract_invalid_file():
    with pytest.raises(FileNotFoundError):
        extract('data/raw/invalid_file.csv')
