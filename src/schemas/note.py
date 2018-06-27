NotePostSchema = {
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 30,
        },
        'text': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 500,
        },
    },
    'required': ['title', 'text'],
}

NotePatchSchema = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'pattern': r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
        },
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 30,
        },
        'text': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 500,
        },
    },
    'required': ['id'],
    'anyOf': [
        {
            'required': ['title'],
        },
        {
            'required': ['text'],
        },
    ],
}

NoteDeleteSchema = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'pattern': r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
        },
    },
    'required': ['id'],
}
