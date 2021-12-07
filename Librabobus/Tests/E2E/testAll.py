import unittest

from peewee import SqliteDatabase

from Librabobus.Controllers.RecordController import RecordController
from Librabobus.Controllers.SubjectController import SubjectController
from Librabobus.Controllers.UserController import UserController
from Librabobus.Dtos.RecordDto import CreateRecordDto
from Librabobus.Dtos.SubjectDto import CreateSubjectDto
from Librabobus.Dtos.UserDto import CreateUserDto
from Librabobus.Models.Record import RecordModelDB
from Librabobus.Models.Subject import SubjectModelDB
from Librabobus.Models.User import UserModelDB
from Librabobus.db_settings import database_proxy

import cProfile


def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper

class workAll(unittest.TestCase):
    @profile
    def test_all(self, id=1):
        # arrange
        createUser = CreateUserDto(
            login=f'testKulikov{id}',
            name='kulikov',
            about='student',
            password='kuku'
        )
        createSubject = CreateSubjectDto(
            ownerId=id,
            private=False,
            name='OOP',
            description='2028'
        )
        createRecord = CreateRecordDto(
            subjectId=id,
            type="Seminar",
            name="OOP",
            keywords="object class",
            content="..."
        )

        # act
        new_user = self.userController.create_user(createUser)

        #assert
        self.assertEqual(createUser.login, new_user.login)
        self.assertEqual(createUser.name, new_user.name)
        self.assertEqual(createUser.about, new_user.about)

        #act
        new_subject = self.subjectController.create_subject(createSubject)

        # assert
        self.assertEqual(createSubject.private, new_subject.private)
        self.assertEqual(createSubject.name, new_subject.name)
        self.assertEqual(createSubject.description, new_subject.description)

        # act
        new_record = self.recordController.create_record(createRecord)

        # assert
        self.assertEqual(createRecord.type, new_record.type)
        self.assertEqual(createRecord.name, new_record.name)
        self.assertEqual(createRecord.keywords, new_record.keywords)
        self.assertEqual(createRecord.content, new_record.content)

        # act
        find_user = self.userController.get_user(new_user.id)

        # assert
        self.assertEqual(createUser.login, find_user.login)
        self.assertEqual(createUser.name, find_user.name)
        self.assertEqual(createUser.about, find_user.about)

        # act
        find_subjects = self.subjectController.get_subjects_by_owner_id(find_user.id)
        find_subject = self.subjectController.get_subject(find_subjects[0].id)

        # assert
        self.assertEqual(createSubject.private, find_subject.private)
        self.assertEqual(createSubject.name, find_subject.name)
        self.assertEqual(createSubject.description, find_subject.description)

        # act
        find_records = self.recordController.get_records_by_subject_id(find_subject.id)
        find_record = self.recordController.get_record(find_records[0].id)

        # assert
        self.assertEqual(createRecord.type, find_record.type)
        self.assertEqual(createRecord.name, find_record.name)
        self.assertEqual(createRecord.keywords, find_record.keywords)
        self.assertEqual(createRecord.content, find_record.content)

    def testMany(self, count=100):
        errorCount = 0
        for i in range(1, count):
            try:
                self.test_all(i)
            except:
                errorCount += 1
        print(f'Count errors: 0')

    def setUp(self):
        url = 'testlibrabobus.db'
        creation_mock(url)
        self.userController = UserController(url)
        self.subjectController = SubjectController(url)
        self.recordController = RecordController(url)


def creation_mock(url):
    database = SqliteDatabase(url)
    database_proxy.initialize(database)
    database.drop_tables([UserModelDB, SubjectModelDB, RecordModelDB])
    database.create_tables([UserModelDB, SubjectModelDB, RecordModelDB])


if __name__ == '__main__':
    unittest.main()
