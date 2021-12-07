from Librabobus.Models.User import UserModelDB
from ..Entities.User import User
from ..Logs.log import logger
from ..db_settings import database_proxy, database_connect


class UserRepository:
    def __init__(self, url):
        # Based on configuration, use a different database.
        self.database = database_connect(url)
        # Configure our proxy to use the db we specified in config.
        database_proxy.initialize(self.database)
        self.UserModelDB = UserModelDB


    def findById(self, id):
        try:
            user = self.UserModelDB.get(UserModelDB.id == id)
            logger.info("User was received")
            return User(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            logger.warning("User wasn't received")
            return None

    def findAll(self):
        users = self.UserModelDB.select()
        result = []
        for user in users:
            result.append(User(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            ))
        logger.info("User was received")
        return result

    def create(self, newUser):
        try:
            user = self.UserModelDB(
                login=newUser.login,
                name=newUser.name,
                about=newUser.about,
                password=newUser.password
            )
            user.save()
            logger.info("User was created")
            return User(
                id=user.id,
                login=user.login,
                name=user.name,
                about=user.about
            )
        except:
            logger.warning("User wasn't created")
            return None

    def update(self, updateUser):
        try:
            user = self.UserModelDB.get(UserModelDB.id == id)
            user.name = updateUser.name,
            user.about = updateUser.about,
            user.save()
            logger.info("User was updated")
            return User(
                id=user.id,
                name=user.name,
                about=user.about
            )
        except:
            logger.warning("User wasn't updated")
            return None

    def delete(self, id):
        try:
            user = self.UserModelDB.get(UserModelDB.id == id)
            logger.info("User was deleted")
            return user.delete_instance()
        except:
            logger.warning("User wasn't deleted")
            return 0