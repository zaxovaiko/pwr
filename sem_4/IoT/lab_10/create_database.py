import sqlite3
import os
import seeder
from dotenv import load_dotenv


def create_database():
    """
    Removes previously created database and report if it exists.
    Creates three tables (records, workers, cards).

    :return: None
    """

    if os.path.exists('records.db'):
        os.remove('records.db')

    if os.path.exists('report.csv'):
        os.remove('report.csv')

    con = sqlite3.connect('records.db')
    con.execute(
        '''
        CREATE TABLE records (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            card_id INT NOT NULL,
            worker_id INT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    con.execute(
        '''
        CREATE TABLE workers (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT NOT NULL,
            card_id INT UNIQUE NULL,
            hired_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    con.execute(
        '''
        CREATE TABLE cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT NOT NULL,
            worker_id INT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    con.commit()
    con.close()
    print('Tables were created successfully.')

    if bool(os.getenv('SEED')):
        seeder.seed_database()


if __name__ == '__main__':
    load_dotenv()
    create_database()
