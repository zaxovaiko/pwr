import sqlite3
import os


def create_database():
    """
    Removes previously created database if it exists.
    Creates three tables (records, workers, cards).

    :return: None
    """

    if os.path.exists('records.db'):
        os.remove('records.db')

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
    print('Tables were created successfully.')
    con.close()


if __name__ == '__main__':
    create_database()
