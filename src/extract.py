import pandas as pd
import logging

def extract(file_path):
    try:
        logging.info("Starting data extraction")
        df = pd.read_csv(file_path)
        logging.debug(df.to_string())
        logging.info("Data extraction completed")
        return df
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        logging.error(f"No data: {e}")
        raise
    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        raise
