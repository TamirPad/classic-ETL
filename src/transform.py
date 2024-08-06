import pandas as pd
import logging
from .utils import validate_data_types, validate_missing_values, validate_ranges, validate_uniqueness, validate_format, \
    validate_business_rules


def transform(df):
    try:
        logging.info("Starting data transformation")
        df['date'] = pd.to_datetime(df['date'])
        df['value'] = df['value'].fillna(0)

        # Data Validation
        validate_data_types(df)
        validate_missing_values(df)
        validate_ranges(df)
        validate_uniqueness(df)
        validate_format(df)
        validate_business_rules(df)

        logging.info("Data transformation completed")
        return df
    except AssertionError as e:
        logging.error(f"Data validation failed: {e}")
        raise
    except KeyError as e:
        logging.error(f"Column not found: {e}")
        raise
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise
