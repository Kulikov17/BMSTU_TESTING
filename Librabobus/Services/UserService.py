from Librabobus.Dtos.UserDto import UserDto
from Librabobus.Entities.User import User
from Librabobus.Repositories.SubjectRepository import SubjectRepository
from Librabobus.Repositories.UserRepository import UserRepository


class UserService:
    def __init__(self, url):
        self.userRepository = UserRepository(url)
        self.subjectRepository = SubjectRepository(url)

    def get_user(self, id):
        try:
            user = self.userRepository.findById(id)
            return UserDto(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            return None

    def get_users(self):
        try:
            users = self.userRepository.findAll()
            result = []
            for user in users:
                result.append(UserDto(
                    id=user.id,
                    login=user.login,
                    name=user.name,
                    about=user.about
                ))
            return result
        except:
            return None

    def create_user(self, createUserDto):
        newUser = User(
            login=createUserDto.login,
            name=createUserDto.name,
            about=createUserDto.about,
            password=createUserDto.password,
        )
        try:
            user = self.userRepository.create(newUser)
            return UserDto(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            return None

    def update_user(self, updateUserDto):
        updateUser = User(
            name=updateUserDto.name,
            about=updateUserDto.about
        )
        try:
            user = self.userRepository.update(updateUser)
            return UserDto(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            return None

    def delete_user(self, id):
        try:
            countDelete = self.userRepository.delete(id)
            return countDelete
        except:
            None