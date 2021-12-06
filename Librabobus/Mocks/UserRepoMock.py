from Librabobus.Tests.TestBuilders.UserBuilder import UserMother


class UserDBRepoMock:

    @staticmethod
    def get(user_id):
        return UserMother.one().build()

    @staticmethod
    def get_all():
        return [UserMother.one().build(), UserMother.two().build()]