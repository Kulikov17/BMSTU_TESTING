from utils.Librabobus.Services.UserService import UserService
from utils.Librabobus.Logs.log import logger

class UserController:
    def __init__(self, url):
        self.userService = UserService(url)

    def get_user(self, id):
        try:
            logger.info("User was received")
            return self.userService.get_user(id)
        except:
            logger.warning("User wasn't got")
            return None

    def get_users(self):
        try:
            logger.info("Users was received")
            return self.userService.get_users()
        except:
            logger.warning("Users wasn't got")
            return None

    def create_user(self, createUserDto):
        try:
            logger.info("Users was created")
            return self.userService.create_user(createUserDto)
        except:
            logger.warning("Users wasn't created")
            return None

    def update_user(self, updateUserDto):
        try:
            logger.info("Users was updated")
            return self.userService.update_user(updateUserDto)
        except:
            logger.warning("Users wasn't updated")
            return None

    def delete_user(self, id):
        try:
            logger.info("Users was deleted")
            return self.userService.delete_user(id)
        except:
            logger.warning("Users wasn't deleted")
            None