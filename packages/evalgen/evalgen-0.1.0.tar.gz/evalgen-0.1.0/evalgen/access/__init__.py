import os
import pandas as pd
import importlib.util
from sqlalchemy import create_engine, inspect

__all__ = [
    'DataSourceLoader',
    'StandardDataSourceLoader'
]

class DataSourceLoader:

    def validate(self):
        pass
    
class StandardDataSourceLoader(DataSourceLoader):

    def __init__(self, source):
        self.source = source

    def validate(self):

        if self.source is None:
            raise Exception("StandardDataSourceLoader requires a path (csv)")

        source = self.source
        if isinstance(source, str) and len(source) == 0:
            raise Exception(f"Invalid source: {source}")

        if ((not os.path.exists(source)) and (source not in os.environ)):
            raise Exception(f"Invalid source: {source}. Path should be valid or be an environment variable")
        
    def load(self):

        source = self.source
        if source in os.environ:
            source = os.environ[source]
            
        if self.source.startswith('sqlite:///') or self.source.startswith('postgresql://'):
            return self._load_from_database()
        elif self.source.endswith('.csv'):
            return pd.read_csv(self.source)
        elif self.source.endswith('.log'):
            return self._load_from_logfile()
        else:
            raise ValueError("Unrecognized source type. Please provide a valid database URL, CSV file, or logfile.")

    def _load_from_database(self):
        engine = create_engine(self.source)
        connection = engine.connect()
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        table = self._prompt_user_for_table(tables)
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, connection)
        connection.close()
        return df

    def _prompt_user_for_table(self, tables):
        print("Available tables:")
        for table in tables:
            print(f"- {table}")
        selected_table = input("Enter the name of the table you want to extract: ")
        while selected_table not in tables:
            print("Invalid table name. Please choose from the available tables.")
            selected_table = input("Enter the name of the table you want to extract: ")
        return selected_table

    def _load_from_logfile(self):
        # Implement logic to parse the logfile and return a DataFrame
        return pd.read_csv(self.source, delimiter=' ', header=None)  # Adjust parsing as needed

    
