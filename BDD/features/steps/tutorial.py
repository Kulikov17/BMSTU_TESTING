from behave import *
from peewee import SqliteDatabase

from utils.Librabobus.Controllers.UserController import UserController
from utils.Librabobus.Controllers.SubjectController import SubjectController
from utils.Librabobus.Models.Record import RecordModelDB
from utils.Librabobus.Models.Subject import SubjectModelDB
from utils.Librabobus.Models.User import UserModelDB
from utils.Librabobus.db_settings import database_proxy

from utils.Librabobus.Dtos.UserDto import CreateUserDto
from utils.Librabobus.Dtos.SubjectDto import CreateSubjectDto


@given('I put user {login} {name} {password} parameters')
def step_impl(context,login, name, password):
    context.create_user = CreateUserDto(
        login=login,
        name=name,
        about='',
        password=password
    )

@when('I make create request')
def step_impl(context):
    userController = UserController('librabobus.db')
    context.created_user = userController.create_user(context.create_user)
    assert True is not False

@then('I should be user with {login} {name}')
def step_impl(context,login, name):
    assert context.created_user.login == login
    assert context.created_user.name == name


@given('I put subject {ownerId} {private} {name} {description} parameters')
def step_impl(context,ownerId, private, name, description):
    context.create_subject = CreateSubjectDto(
        ownerId=int(ownerId),
        private = bool(private),
        name=name,
        description = description
    )

@when('I make create subject request')
def step_impl(context):
    subjectController = SubjectController('librabobus.db')
    context.created_subject = subjectController.create_subject(context.create_subject)
    assert True is not False

@then('I should be subject with {ownerId} {private} {name} {description}')
def step_impl(context, ownerId, private, name, description):
    assert str(context.created_subject.ownerId) == str(ownerId)
    assert context.created_subject.private == bool(private)
    assert context.created_subject.name == name
    assert context.created_subject.description == description


def creation():
    # Based on configuration, use a different database.
    database = SqliteDatabase('librabobus.db')
    # Configure our proxy to use the db we specified in config.
    database_proxy.initialize(database)
    database.drop_tables([UserModelDB, SubjectModelDB, RecordModelDB])
    database.create_tables([UserModelDB, SubjectModelDB, RecordModelDB])

creation()