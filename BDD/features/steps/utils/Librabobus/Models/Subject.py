from peewee import PrimaryKeyField, CharField, ForeignKeyField, BooleanField, DateTimeField
from utils.Librabobus.Models.BaseModel import BaseModel
from utils.Librabobus.Models.User import UserModelDB

class SubjectModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    ownerId = ForeignKeyField(UserModelDB, to_field="id")
    private = BooleanField(default=False)
    name = CharField(null=False)
    description = CharField()