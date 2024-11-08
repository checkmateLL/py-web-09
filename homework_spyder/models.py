from datetime import datetime
from mongoengine import Document, EmbeddedDocument, ReferenceField
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {'collection': 'authors'}

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'collection': 'quotes'}