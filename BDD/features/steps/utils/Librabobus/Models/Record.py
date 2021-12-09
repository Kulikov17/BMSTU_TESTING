from peewee import PrimaryKeyField, ForeignKeyField, DateTimeField, CharField
from utils.Librabobus.Models.BaseModel import BaseModel
from utils.Librabobus.Models.Subject import SubjectModelDB


class RecordModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    subjectId = ForeignKeyField(SubjectModelDB, to_field="id")
    type = CharField(null=False)
    name = CharField(null=False)
    keywords = CharField()
    content = CharField()