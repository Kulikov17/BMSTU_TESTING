from Librabobus.Services.UserService import UserService


class UserController:
    def __init__(self, url):
        self.userService = UserService(url)

    def get_user(self, id):
        try:
            return self.userService.get_user(id)
        except:
            return None

    def get_users(self):
        try:
            return self.userService.get_users()
        except:
            return None

    def create_user(self, createUserDto):
        try:
            return self.userService.create_user(createUserDto)
        except:
            return None

    def update_user(self, updateUserDto):
        try:
            return self.userService.update_user(updateUserDto)
        except:
            return None

    def delete_user(self, id):
        try:
            return self.userService.delete_user(id)
        except:
            None