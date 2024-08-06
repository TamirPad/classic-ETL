from src.extract import extract
from src.transform import transform
from src.load import load
from src.config import FILE_PATH, DB_CONNECTION_STRING
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        data = extract(FILE_PATH)
        transformed_data = transform(data)
        load(transformed_data, DB_CONNECTION_STRING)
        logging.info("ETL process completed successfully")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()
