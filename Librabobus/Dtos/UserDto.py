class UserDto:
    def __init__(self, id, login, name, about):
        self.id = id
        self.login = login
        self.name = name
        self.about = about

class CreateUserDto:
    def __init__(self, login, password, name, about):
        self.login = login
        self.password = password
        self.name = name
        self.about = about