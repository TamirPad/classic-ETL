import pandas as pd
import re
import logging

def validate_data_types(df):
    assert pd.api.types.is_datetime64_any_dtype(df['date']), "Date column should be datetime"
    assert pd.api.types.is_numeric_dtype(df['value']), "Value column should be numeric"

def validate_missing_values(df):
    assert df['date'].notnull().all(), "Date column has missing values"
    assert df['value'].notnull().all(), "Value column has missing values"

def validate_ranges(df):
    assert df['value'].between(0, 10000).all(), "Value column has out-of-range values"

def validate_uniqueness(df):
    assert df['id'].is_unique, "ID column has duplicate values"

def validate_format(df):
    email_pattern = r'^[\w\.-]+@[\w\.-]+$'
    assert df['email'].str.match(email_pattern).all(), "Email column has invalid formats"

def validate_business_rules(df):
    assert (df['start_date'] <= df['end_date']).all(), "Start date should be before end date"
