import sqlite3
import os


def create_database():
    # Remove previous database
    if os.path.exists('records.db'):
        os.remove('records.db')

    con = sqlite3.connect('records.db')
    con.execute(
        '''
        CREATE TABLE records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id INT NOT NULL,
            worker_id INT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    con.execute(
        '''
        CREATE TABLE workers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            card_id INT UNIQUE DEFAULT -1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    con.commit()
    print('Tables records and workers were created successfully.')
    con.close()


if __name__ == '__main__':
    create_database()
