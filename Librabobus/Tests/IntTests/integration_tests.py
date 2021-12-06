import unittest
from unittest.mock import Mock

import peewee

from Librabobus.Models.Record import RecordModelDB
from Librabobus.Models.Subject import SubjectModelDB
from Librabobus.Models.User import UserModelDB
from Librabobus.Services.RecordService import RecordService
from Librabobus.Services.SubjectService import SubjectService
from Librabobus.Services.UserService import UserService
from Librabobus.Tests.TestBuilders.RecordBuilder import RecordBuilder
from Librabobus.Tests.TestBuilders.SubjectBuilder import SubjectBuilder
from Librabobus.Tests.TestBuilders.UserBuilder import UserBuilder
from Librabobus.db_settings import database_proxy


class TestUserAndSubjectService(unittest.TestCase):
    def test_create_user_and_subject_positive(self):
        #arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()
        subject = SubjectBuilder(id=1, ownerId=user.id, name='test').build()

        #act
        new_user = self.userService.create_user(user)
        new_subject = self.subjectService.create_subject(subject)

        #assert
        self.assertEqual(user.login, new_user.login)
        self.assertEqual(user.name, new_user.name)
        self.assertEqual(str(subject.ownerId), str(new_subject.ownerId))
        self.assertEqual(subject.name, new_subject.name)

    def setUp(self):
        creation_mock()
        self.userService = UserService('mocklibrabobus.db')
        self.subjectService = SubjectService('mocklibrabobus.db')


class TestUserAndSubjectAndRecordService(unittest.TestCase):
    def test_create_user_and_subject_and_record_positive(self):
        # arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()
        subject = SubjectBuilder(id=1, ownerId=user.id, name='test').build()
        record = RecordBuilder(id=1, subjectId=subject.id, name='test').build()

        # act
        new_user = self.userService.create_user(user)
        new_subject = self.subjectService.create_subject(subject)
        new_record = self.recordService.create_record(record)

        # assert
        self.assertEqual(user.login, new_user.login)
        self.assertEqual(user.name, new_user.name)
        self.assertEqual(str(subject.ownerId), str(new_subject.ownerId))
        self.assertEqual(subject.name, new_subject.name)
        self.assertEqual(str(record.subjectId), str(new_record.subjectId))
        self.assertEqual(record.name, new_record.name)

    def setUp(self):
        creation_mock()
        self.userService = UserService('mocklibrabobus.db')
        self.subjectService = SubjectService('mocklibrabobus.db')
        self.recordService = RecordService('mocklibrabobus.db')

def creation_mock():
    database = peewee.SqliteDatabase('mocklibrabobus.db')
    database_proxy.initialize(database)
    database.drop_tables([UserModelDB, SubjectModelDB, RecordModelDB])
    database.create_tables([UserModelDB, SubjectModelDB, RecordModelDB])


if __name__ == '__main__':
    unittest.main()
