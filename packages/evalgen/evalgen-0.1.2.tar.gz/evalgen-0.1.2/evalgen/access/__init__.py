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
            raise Exception("StandardDataSourceLoader requires a valid path/url")

        source = self.source
        if isinstance(source, str) and len(source) == 0:
            raise Exception(f"Invalid source: {source}")

        if ((not os.path.exists(source)) and (source not in os.environ)):
            raise Exception(f"Invalid source: {source}. Path should be valid or be an environment variable")

    def load(self, spec=None):

        source = self.source
        if source in os.environ:
            source = os.environ[source]

        if source.startswith('sqlite:///') or source.startswith('postgresql://'):
            return self._load_from_database(source, spec)
        elif source.endswith('.csv'):
            return pd.read_csv(self.source), {}
        elif source.endswith('.log'):
            return self._load_from_logfile(), {}
        else:
            raise ValueError("Unrecognized source type. Please provide a valid database URL, CSV file, or logfile.")

    def _load_from_database(self, source, spec=None):

        engine = create_engine(source)
        connection = engine.connect()
        if spec is not None and hasattr(spec, 'get_query_params'):
            query_params = spec.get_query_params()
        else:
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            table = self._prompt_user_for_table(tables)
            query_params = {
                "table": table,
                "limit": 1000
            }
        query = f"SELECT * FROM %(table)s limit %(limit)s" % query_params

        df = pd.read_sql(query, connection)
        connection.close()
        return df, query_params

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


