import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')

if all((DATABASE_USERNAME,
        DATABASE_PASSWORD,
        DATABASE_HOST,
        DATABASE_PORT,
        DATABASE_NAME,)):
    SQLALCHEMY_DATABASE_URI = \
        ('postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
            .format(
                username=DATABASE_USERNAME,
                password=DATABASE_PASSWORD,
                host=DATABASE_HOST,
                port=DATABASE_PORT,
                database=DATABASE_NAME,
            ))
else:
    raise ValueError('Database credentials are not specified')

JSON_SORT_KEYS = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
