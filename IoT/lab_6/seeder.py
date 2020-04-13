import sqlite3
from faker import Faker


def seed_database():
    fake = Faker()

    con = sqlite3.connect('records.db')

    for i in range(1000):
        con.execute(f'INSERT INTO workers (name) VALUES ("{fake.name()}")')

    con.commit()
    print('Tables was seeded successfully.')
    con.close()


if __name__ == '__main__':
    seed_database()
