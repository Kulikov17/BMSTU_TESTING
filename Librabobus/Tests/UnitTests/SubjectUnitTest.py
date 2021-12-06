import unittest

from peewee import SqliteDatabase, IntegrityError

from Librabobus.Models.Record import RecordModelDB
from Librabobus.Models.Subject import SubjectModelDB
from Librabobus.Models.User import UserModelDB
from Librabobus.Repositories.SubjectRepository import SubjectRepository
from Librabobus.Repositories.UserRepository import UserRepository
from Librabobus.Tests.TestBuilders.SubjectBuilder import SubjectBuilder
from Librabobus.Tests.TestBuilders.UserBuilder import UserBuilder
from Librabobus.db_settings import database_proxy


class AddSubjectTestSuite(unittest.TestCase):
    def test_create_user_positive(self):
        #arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()
        new_user = self.userRepository.create(user)
        subject = SubjectBuilder(id=1, ownerId=new_user.id, name='test').build()

        #act
        new_subject = self.subjectRepository.create(subject)

        #assert
        self.assertEqual(str(subject.ownerId), str(new_subject.ownerId))
        self.assertEqual(subject.name, new_subject.name)

    def test_create_subject_negative(self):
        #arrange
        subject = SubjectBuilder(id=1, ownerId=1, name='test').build()

        #act
        new_subject = self.subjectRepository.create(subject)

        #assert
        self.assertIsNone(new_subject)


    def setUp(self):
        creation_mock()
        self.userRepository = UserRepository('mocklibrabobus.db')
        self.subjectRepository = SubjectRepository('mocklibrabobus.db')


class DeleteSubjectTestSuite(unittest.TestCase):
    def test_delete_subject_positive(self):
        # arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()
        new_user = self.userRepository.create(user)
        subject = SubjectBuilder(id=1, ownerId=new_user.id, name='test').build()

        # act
        new_subject = self.subjectRepository.create(subject)
        countDelete = self.subjectRepository.delete(new_subject.id)
        subject = self.subjectRepository.findById(new_subject.id)

        # assert
        self.assertEqual(1, countDelete)
        self.assertIsNone(subject)

    def test_delete_subject_negative(self):
        # arrange
        id = 0

        # act
        delete_subject = self.subjectRepository.delete(id)
        subject = self.subjectRepository.findById(id)

        # assert
        self.assertIsNone(delete_subject)
        self.assertIsNone(subject)

    def setUp(self):
        creation_mock()
        self.userRepository = UserRepository('mocklibrabobus.db')
        self.subjectRepository = SubjectRepository('mocklibrabobus.db')


class FindUserTestSuite(unittest.TestCase):
    def test_find_user_positive(self):
        # arrange
        user = UserBuilder(id=1, login='test3@bmstu.ru', name='test', password='test').build()

        # act
        new_user = self.userRepository.create(user)
        userFind = self.userRepository.findById(new_user.id)

        # assert
        self.assertEqual(userFind.id, new_user.id)
        self.assertEqual(str(userFind.login), str(new_user.login))
        self.assertEqual(str(userFind.name), str(new_user.name))

    def test_find_user_negative(self):
        # arrange
        id = 0

        # act
        user = self.userRepository.findById(id)

        # assert
        self.assertIsNone(user)

    def setUp(self):
        creation_mock()
        self.userRepository = UserRepository('mocklibrabobus.db')

def creation_mock():
    database = SqliteDatabase('mocklibrabobus.db')
    database_proxy.initialize(database)
    database.drop_tables([UserModelDB, SubjectModelDB, RecordModelDB])
    database.create_tables([UserModelDB, SubjectModelDB, RecordModelDB])

if __name__ == '__main__':
    unittest.main()