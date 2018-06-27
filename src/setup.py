from database import db
from models import *


def create():
    db.create_all()


def insert():
    db.session.add(Note(title='Первая заметка', text='Первая заметка'))
    db.session.add(Note(title='Вторая заметка', text='Вторая заметка'))
    db.session.commit()


if __name__ == '__main__':
    create()
    insert()
