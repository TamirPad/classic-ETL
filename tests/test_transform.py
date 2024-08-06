import pytest
import pandas as pd
from src.transform import transform

def test_transform_valid_data():
    df = pd.DataFrame({
        'date': ['2024-01-01'],
        'value': [10],
        'id': [1],
        'email': ['test@example.com'],
        'start_date': ['2024-01-01'],
        'end_date': ['2024-01-02']
    })
    transformed_df = transform(df)
    assert pd.api.types.is_datetime64_any_dtype(transformed_df['date']), "Date column should be datetime"
    assert transformed_df['value'].notnull().all(), "Value column should not have missing values"
