import unittest

#from Librabobus.Repositories.UserRepository import UserRepository
from peewee import SqliteDatabase, IntegrityError

from Librabobus.Models.Record import RecordModelDB
from Librabobus.Models.Subject import SubjectModelDB
from Librabobus.Models.User import UserModelDB
from Librabobus.Repositories.UserRepository import UserRepository
from Librabobus.Tests.TestBuilders.UserBuilder import UserBuilder
from Librabobus.db_settings import database_proxy


class AddUserTestSuite(unittest.TestCase):
    def test_create_user_positive(self):
        #arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()
        #act
        new_user = self.userRepository.create(user)
        #assert
        self.assertEqual(user.id, new_user.id)
        self.assertEqual(user.login, new_user.login)
        self.assertEqual(user.name, new_user.name)

    def test_create_user_negative(self):
        #arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()
        #assert
        with (self.assertRaises(IntegrityError)):
            #act
            self.userRepository.create(user)
            self.userRepository.create(user)

    def setUp(self):
        creation_mock()
        self.userRepository = UserRepository('mocklibrabobus.db')


class DeleteUserTestSuite(unittest.TestCase):
    def test_delete_user_positive(self):
        # arrange
        user = UserBuilder(id=1, login='test15@bmstu.ru', name='test', password='test').build()

        # act
        new_user = self.userRepository.create(user)
        countDelete = self.userRepository.delete(new_user.id)
        user = self.userRepository.findById(new_user.id)

        # assert
        self.assertEqual(1, countDelete)
        self.assertIsNone(user)

    def test_delete_user_negative(self):
        # arrange
        id = 0

        # act
        countDelete = self.userRepository.delete(id)
        user = self.userRepository.findById(id)

        # assert
        self.assertEqual(0, countDelete)
        self.assertIsNone(user)

    def setUp(self):
        creation_mock()
        self.userRepository = UserRepository('mocklibrabobus.db')


class FindUserTestSuite(unittest.TestCase):
    def test_find_user_positive(self):
        # arrange
        user = UserBuilder(id=1, login='test3@bmstu.ru', name='test', password='test').build()

        # act
        new_user = self.userRepository.create(user)
        userFind = self.userRepository.findById(new_user.id)

        # assert
        self.assertEqual(userFind.id, new_user.id)
        self.assertEqual(userFind.login, new_user.login)
        self.assertEqual(userFind.name, new_user.name)

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

class UpdateUserTestSuite(unittest.TestCase):
    def test_update_user_positive(self):
        #arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()

        #act
        update_user = self.userRepository.update(user)

        # assert
        self.assertIsNone(update_user)

    def test_update_user_negative(self):
        #arrange
        user = UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build()
        #assert
        with (self.assertRaises(IntegrityError)):
            #act
            self.userRepository.create(user)
            self.userRepository.create(user)

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
