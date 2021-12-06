import unittest
from unittest.mock import Mock

from Librabobus.Dtos.UserDto import UserDto, CreateUserDto
from Librabobus.Services.UserService import UserService
from Librabobus.Tests.TestBuilders.UserBuilder import UserBuilder


class AddUserTestSuite(unittest.TestCase):
    def test_create_user_positive(self):
        #arrange
        user = CreateUserDto(
                login='test@bmstu.ru',
                name='test',
                password='test',
                about=''
            )

        #act
        new_user = self.userService.create_user(user)

        # assert
        self.mockCreate.assert_called()
        self.assertEqual(user.login, new_user.login)
        self.assertEqual(user.name, new_user.name)
        self.assertEqual(user.about, new_user.about)

    def test_create_user_negative(self):
        #arrange
        user = CreateUserDto(
                login='test@bmstu.ru',
                name='test',
                password='test',
                about=''
            )
        self.userService.userRepository.create = self.stub

        #act
        new_user = self.userService.create_user(user)

        # assert
        self.assertIsNone(new_user)

    def stub(self):
        return None

    def setUp(self):
        self.userService = UserService('tmp')
        self.mockCreate = Mock(return_value=UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build())
        self.userService.userRepository.create = self.mockCreate


class FindUserTestSuite(unittest.TestCase):
    def test_find_user_positive(self):
        # arrange
        user = UserDto(
            id = 1,
            login='test@bmstu.ru',
            name='test',
            about=''
        )

        # act
        find_user = self.userService.get_user(user.id)

        # assert
        self.mockFind.assert_called()
        self.assertEqual(user.id, find_user.id)
        self.assertEqual(user.login, find_user.login)
        self.assertEqual(user.name, find_user.name)
        self.assertEqual(user.about, find_user.about)

    def test_find_user_negative(self):
        # arrange
        user = UserDto(
            id=1,
            login='test@bmstu.ru',
            name='test',
            about=''
        )
        self.userService.userRepository.findById = self.stub

        # act
        find_user = self.userService.get_user(user.id)

        # assert
        self.assertIsNone(find_user)

    def stub(self):
        return None

    def setUp(self):
        self.userService = UserService('tmp')
        self.mockFind = Mock(
            return_value=UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build())
        self.userService.userRepository.findById = self.mockFind


class UpdateUserTestSuite(unittest.TestCase):
    def test_update_user_positive(self):
        # arrange
        user = UserDto(
            id = 1,
            login='test@bmstu.ru',
            name='test',
            about=''
        )

        # act
        update_user = self.userService.update_user(user)

        # assert
        self.mockUpdate.assert_called()
        self.assertEqual(user.id, update_user.id)
        self.assertEqual(user.login, update_user.login)
        self.assertEqual(user.name, update_user.name)
        self.assertEqual(user.about, update_user.about)

    def test_update_user_negative(self):
        # arrange
        user = UserDto(
            id=1,
            login='test@bmstu.ru',
            name='test',
            about=''
        )
        self.userService.userRepository.update = self.stub

        # act
        update_user = self.userService.update_user(user)

        # assert
        self.assertIsNone(update_user)

    def stub(self):
        return None

    def setUp(self):
        self.userService = UserService('tmp')
        self.mockUpdate = Mock(
            return_value=UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build())
        self.userService.userRepository.update = self.mockUpdate


class DeleteUserTestSuite(unittest.TestCase):
    def test_delete_user_positive(self):
        # arrange
        user = UserDto(
            id = 1,
            login='test@bmstu.ru',
            name='test',
            about=''
        )

        # act
        delete_user = self.userService.delete_user(user)

        # assert
        self.mockDelete.assert_called()
        self.assertEqual(user.id, delete_user.id)
        self.assertEqual(user.login, delete_user.login)
        self.assertEqual(user.name, delete_user.name)
        self.assertEqual(user.about, delete_user.about)

    def test_delete_user_negative(self):
        # arrange
        user = UserDto(
            id = 1,
            login='test@bmstu.ru',
            name='test',
            about=''
        )
        self.userService.userRepository.delete = self.stub

        # act
        delete_user = self.userService.delete_user(user)

        # assert
        self.assertIsNone(delete_user)


    def stub(self):
        return 0

    def setUp(self):
        self.userService = UserService('tmp')
        self.mockDelete = Mock(
            return_value=UserBuilder(id=1, login='test@bmstu.ru', name='test', password='test').build())
        self.userService.userRepository.delete = self.mockDelete

if __name__ == '__main__':
    unittest.main()
