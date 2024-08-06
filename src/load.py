from sqlalchemy import create_engine, exc
import logging

def load(df, db_connection_string):
    try:
        logging.info("Starting data loading")
        engine = create_engine(db_connection_string)
        df.to_sql('my_table', con=engine, if_exists='replace', index=False)
        logging.info("Data loading completed")
    except exc.SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        raise
    except Exception as e:
        logging.error(f"Error during data loading: {e}")
        raise
