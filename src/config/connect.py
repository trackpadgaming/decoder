import psycopg2
from config import configLoader

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print('SQL Connected')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    config = configLoader()
    connect(config)