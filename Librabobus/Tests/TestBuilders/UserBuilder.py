from Librabobus.Entities.User import User


class UserBuilder:
    def __init__(self, id, login, name, password):
        self.id = id
        self.login = login
        self.name = name
        self.about = ""
        self.password = password

    def withAbout(self, new_about):
        self.about = new_about


    def build(self):
        return User(
            id = self.id,
            login=self.login,
            name=self.name,
            about=self.about,
            password=self.password
        )
