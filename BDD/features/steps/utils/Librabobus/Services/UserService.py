from utils.Librabobus.Dtos.UserDto import UserDto
from utils.Librabobus.Entities.User import User
from utils.Librabobus.Repositories.SubjectRepository import SubjectRepository
from utils.Librabobus.Repositories.UserRepository import UserRepository
from utils.Librabobus.Logs.log import logger

class UserService:
    def __init__(self, url):
        self.userRepository = UserRepository(url)
        self.subjectRepository = SubjectRepository(url)

    def get_user(self, id):
        try:
            user = self.userRepository.findById(id)
            logger.info("User was received")
            return UserDto(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            logger.warning("User wasn't received")
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
            logger.info("User was received")
            return result
        except:
            logger.warning("User wasn't received")
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
            logger.info("User was created")
            return UserDto(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            logger.warning("User wasn't created")
            return None

    def update_user(self, updateUserDto):
        updateUser = User(
            name=updateUserDto.name,
            about=updateUserDto.about
        )
        try:
            user = self.userRepository.update(updateUser)
            logger.info("User was updated")
            return UserDto(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            logger.warning("User wasn't updated")
            return None

    def delete_user(self, id):
        try:
            countDelete = self.userRepository.delete(id)
            logger.info("User was deleted")
            return countDelete
        except:
            logger.warning("User wasn't deleted")
            return None