import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.load import load


@patch('src.load.create_engine')
def test_load(mock_create_engine):
    # Create a mock engine object
    mock_engine = MagicMock()
    # Configure the mock create_engine to return the mock engine
    mock_create_engine.return_value = mock_engine

    # Create a sample DataFrame
    df = pd.DataFrame({'id': [1], 'value': [10]})

    # Call the load function
    load(df, 'sqlite:///mydatabase.db')

    # Assert that create_engine was called with the correct connection string
    mock_create_engine.assert_called_once_with('sqlite:///mydatabase.db')

    # Assert that to_sql was called on the DataFrame with the correct parameters
    df.to_sql = MagicMock()
    df.to_sql('my_table', con=mock_engine, if_exists='replace', index=False)
    df.to_sql.assert_called_once_with('my_table', con=mock_engine, if_exists='replace', index=False)
