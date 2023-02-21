import psycopg2
from contextlib import contextmanager
from sreality_scraper.settings import HOST, DB_NAME, USER, PASSWORD


class Database:

    def __init__(self):
        self.table_name = 'sreality_items'

    @contextmanager
    def connect_to_db(self):
        try:
            self.connection = psycopg2.connect(
            host=HOST,
            database=DB_NAME,
            user=USER,
            password=PASSWORD)
            self.cursor = self.connection.cursor()
            yield None
        finally:
            self.connection.close()

    def delete_all_items(self):
        with self.connect_to_db():
            self.cursor.execute(f'DELETE FROM {self.table_name}')
            self.connection.commit()
    
    def insert_item(self, name, image):
        with self.connect_to_db():
            self.cursor.execute(f"INSERT INTO {self.table_name} (name,image) VALUES (%s,%s)", (str(name), str(image)))
            self.connection.commit()

    def load_all_items(self):
        with self.connect_to_db():
            self.cursor.execute(f"SELECT * FROM {self.table_name}")
            items = self.cursor.fetchall()        
        return items
    
    def create_table_if_doesnt_exist(self):
        with self.connect_to_db():
            self.cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';")
            tables = self.cursor.fetchall()
            tables = [table[0] for table in tables]
            if not self.table_name in tables:
                self.create_table()
    
    def create_table(self):
        with self.connect_to_db():
            self.cursor.execute(f"""
                        create table {self.table_name}
                        (
                            id    serial
                                primary key
                                unique,
                            name  varchar(255),
                            image varchar(255)
                        );
            """)
            self.connection.commit()

            
database  =  Database()
