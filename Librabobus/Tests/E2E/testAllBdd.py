from peewee import SqliteDatabase
from behave import given, when, then

from Librabobus.Controllers.RecordController import RecordController
from Librabobus.Controllers.SubjectController import SubjectController
from Librabobus.Controllers.UserController import UserController
from Librabobus.Models.Record import RecordModelDB
from Librabobus.Models.Subject import SubjectModelDB
from Librabobus.Models.User import UserModelDB
from Librabobus.db_settings import database_proxy


@given(u'Create User')
def test_create_user():
    pass


@given(u'I input login:"{login}", name:"{name}",  password:"{password}", about: "{about}"')
def test_create_user(context,login, name, password, about):
    print(context)
    print(login)
    #new_user = userController.create_user(createUser)




url = 'testlibrabobus.db'
database = SqliteDatabase(url)
database_proxy.initialize(database)
database.drop_tables([UserModelDB, SubjectModelDB, RecordModelDB])
database.create_tables([UserModelDB, SubjectModelDB, RecordModelDB])
userController = UserController(url)
subjectController = SubjectController(url)
recordController = RecordController(url)