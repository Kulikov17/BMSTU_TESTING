from peewee import PrimaryKeyField, ForeignKeyField, DateTimeField, CharField
from Librabobus.Models.BaseModel import BaseModel
from Librabobus.Models.Subject import SubjectModelDB


class RecordModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    subjectId = ForeignKeyField(SubjectModelDB, to_field="id")
    type = CharField(null=False)
    name = CharField(null=False)
    keywords = CharField()
    content = CharField()