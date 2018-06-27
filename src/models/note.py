import uuid
from datetime import datetime
from database import db
from database.types import UUID


class Note(db.Model):
    id = db.Column(UUID, primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(30), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    date_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def as_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'text': self.text,
            'date_create': int(self.date_create.timestamp()),
            'date_update': int(self.date_update.timestamp()),
        }
