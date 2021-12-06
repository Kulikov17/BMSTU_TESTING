from peewee import PrimaryKeyField, CharField
from Librabobus.Models.BaseModel import BaseModel


class UserModelDB(BaseModel):
    id = PrimaryKeyField(null=False)
    login = CharField(unique=True)
    name = CharField(null=False)
    about = CharField()
    password = CharField(null=False)
