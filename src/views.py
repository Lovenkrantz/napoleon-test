from datetime import datetime
from flask import jsonify, Response, request
from jsonschema import validate
from werkzeug.exceptions import BadRequest, NotFound
from app import app
from database import db
from models import Note
from schemas import NoteDeleteSchema, NotePatchSchema, NotePostSchema


def validate_json_body(validator):
    try:
        json = request.get_json()
        validate(json, validator)
    except Exception as exc:
        app.logger.info(exc)
        raise BadRequest(description=exc)
    else:
        return json


@app.route('/', methods=['GET'])
def notes_get():
    result = [
        note.as_dict()
        for note in db.session.query(Note).order_by(Note.date_create).all()
    ]
    return jsonify(result)


@app.route('/', methods=['POST'])
def notes_post():
    json = validate_json_body(NotePostSchema)
    db.session.add(Note(**json))
    db.session.commit()
    return Response(status=201)


@app.route('/', methods=['PATCH'])
def notes_patch():
    json = validate_json_body(NotePatchSchema)
    note = db.session.query(Note).filter_by(id=json['id']).first()
    if note is None:
        raise NotFound()
    # If title or text is not provided in the request,
    # use original ones from the note object.
    note.title = json.setdefault('title', note.title)
    note.text = json.setdefault('text', note.text)
    note.date_update = datetime.utcnow()
    db.session.commit()
    return Response(status=200)


@app.route('/', methods=['DELETE'])
def notes_delete():
    json = validate_json_body(NoteDeleteSchema)
    note = db.session.query(Note).filter_by(id=json['id']).first()
    if note is None:
        raise NotFound()
    db.session.delete(note)
    db.session.commit()
    return Response(status=200)
