import sqlite3
from faker import Faker


def seed_database():
    """
    Use this method to fill database with fake data.
    Faker lib is used to add worker's and card's name.

    :return: None
    """

    fake = Faker('pl_PL')
    Faker.seed(0)
    con = sqlite3.connect('records.db')

    for _ in range(1000):
        con.execute(f'INSERT INTO workers (name) VALUES ("{fake.name()}")')
        con.execute(f'INSERT INTO cards (name) VALUES ("Card {fake.word()}")')

    con.commit()
    con.close()
    print('Tables were seeded successfully.')


if __name__ == '__main__':
    seed_database()
