import sqlite3
from os import path, remove
from config import CONFIG


def create_database():
    con = sqlite3.connect(CONFIG['DATABASE'])

    def create_cards_table():
        con.execute('CREATE ')

    def create_terminals_table():
        pass

    def create_workers_table():
        pass

    def create_records_table():
        pass

    tables = [
        ('cards', create_cards_table),
        ('workers', create_workers_table),
        ('terminals', create_terminals_table),
        ('records', create_records_table)
    ]

    if path.exists(f'./{CONFIG["DATABASE"]}'):
        os.remove(C)

    for table_name, table_func in tables:
        table_func()
        print(f'Table {table_name} was created successfully.')


if __name__ == '__main__':
    create_database()
