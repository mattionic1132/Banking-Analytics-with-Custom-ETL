"""
Database connection and utility functions
"""
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
import pandas as pd
from pathlib import Path
import config


class DatabaseManager:
    """Manages database connections and operations"""
    
    def __init__(self, db_path=None):
        self.db_path = db_path or config.DATABASE_PATH
        self.db_url = f'sqlite:///{self.db_path}'
        
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def get_engine(self):
        return create_engine(
            self.db_url,
            connect_args={'check_same_thread': False},
            poolclass=StaticPool
        )
    
    def execute_sql_file(self, sql_file_path):
        with open(sql_file_path, 'r') as f:
            sql_script = f.read()
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.executescript(sql_script)
            conn.commit()
            print(f"Successfully executed {sql_file_path}")
        except Exception as e:
            conn.rollback()
            print(f"Error executing {sql_file_path}: {e}")
            raise
        finally:
            conn.close()
    
    def query_to_dataframe(self, query, params=None):
        conn = self.get_connection()
        try:
            df = pd.read_sql_query(query, conn, params=params)
            return df
        finally:
            conn.close()
    
    def insert_dataframe(self, df, table_name, if_exists='append'):
        engine = self.get_engine()
        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
        print(f"Inserted {len(df)} rows into {table_name}")
    
    def get_table_count(self, table_name):
        query = f"SELECT COUNT(*) as count FROM {table_name}"
        result = self.query_to_dataframe(query)
        return result['count'].iloc[0]
    
    def list_tables(self):
        query = """
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name
        """
        result = self.query_to_dataframe(query)
        return result['name'].tolist()


def initialize_database(schema_file=None):
    if schema_file is None:
        schema_file = config.PROJECT_ROOT / 'sql' / 'schema.sql'
    
    db_manager = DatabaseManager()
    db_manager.db_path.parent.mkdir(parents=True, exist_ok=True)
    db_manager.execute_sql_file(schema_file)
    
    print(f"Database initialized at {db_manager.db_path}")
    print(f"Tables created: {db_manager.list_tables()}")


if __name__ == "__main__":
    initialize_database()