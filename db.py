from mongoengine import connect, Document, EmbeddedDocument, EmbeddedDocumentListField, IntField, DateTimeField, FloatField

from settings import DB_NAME


class KeepaliveRecord(EmbeddedDocument):
    datetime = DateTimeField(required=True)


class LocationRecord(EmbeddedDocument):
    lat = FloatField(required=True)
    lng = FloatField(required=True)


class Device(Document):
    meta = {'strict': False}
    id = IntField(required=True, min_value=0)
    locations = EmbeddedDocumentListField(LocationRecord, default=[])
    keepalive = EmbeddedDocumentListField(KeepaliveRecord, default=[])


connect(DB_NAME)
