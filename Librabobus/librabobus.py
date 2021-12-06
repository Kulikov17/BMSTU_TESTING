from peewee import SqliteDatabase

from Librabobus.Controllers.RecordController import RecordController
from Librabobus.Controllers.SubjectController import SubjectController
from Librabobus.Controllers.UserController import UserController
from Librabobus.Dtos.UserDto import CreateUserDto
from Librabobus.Models.Record import RecordModelDB
from Librabobus.Models.Subject import SubjectModelDB
from Librabobus.Models.User import UserModelDB
from Librabobus.db_settings import database_proxy


class ConsoleApp:
    def __init__(self, url='librabobus.db'):
        self.userController = UserController(url)
        self.subjectController = SubjectController(url)
        self.recordController = RecordController(url)

    @staticmethod
    def menu():
        print("Консольное приложение:")
        print(" 1) Добавить пользователя")
        print(" 2) Найти пользователя")
        print(" 3) Найти всех пользователей")
        print(" 4) Добавить пользователя")
        print(" 5) Обновить пользователя")
        print(" 6) Удалить пользователя")
        print(" 7) Найти предмет")
        print(" 8) Найти все предметы")
        print(" 9) Добавить предмет")
        print(" 10) Обновить предмет")
        print(" 11) Удалить предмет")
        print(" 12) Найти запись")
        print(" 13) Найти все записи")
        print(" 14) Добавить запись")
        print(" 15) Обновить запись")
        print(" 16) Удалить запись")
        print(" 17) Создать запись и пользователя")
        print(" 18) Вывести все записи по предмету")
        print(" 0) Выйти")

    @staticmethod
    def print_user(user):
        print()
        print(f"id: {user.id}")
        print(f"login: {user.login}")
        print(f"name: {user.name}")
        print(f"about: {user.about}")

    @staticmethod
    def print_subject(subject):
        print()
        print(f"id: {subject.id}")
        print(f"ownerId: {subject.ownerId}")
        print(f"private: {subject.private}")
        print(f"name: {subject.name}")
        print(f"description: {subject.description}")

    @staticmethod
    def print_record(record):
        print()
        print(f"id: {record.id}")
        print(f"subjectId: {record.subjectId}")
        print(f"type: {record.type}")
        print(f"name: {record.name}")
        print(f"keywords: {record.keywords}")
        print(f"content: {record.content}")

    def get_user(self):
        id = int(input("Введите id: "))
        self.print_user(self.userController.get_user(id))

    def get_users(self):
        try:
            users = self.userController.get_users()
            for user in users:
                self.print_user(user)
        except:
            print("Ошибка")

    def get_subject(self):
        id = int(input("Введите id: "))
        try:
            self.print_subject(self.subjectController.get_subject(id))
        except:
            print("Ошибка")


    def get_subjects(self):
        subjects = self.subjectController.get_subjects()
        for subject in subjects:
            self.print_subject(subject)

    def add_user(self):
        login = input("Придумайте логин: ")
        name = input("Введите никнейм: ")
        about = input("Введите информацию о себе: ")
        password = input("Придумайте пароль: ")
        try:
            user = self.userController.create_user(CreateUserDto(
                login=login,
                name=name,
                about=about,
                password=password
            ))
            self.print_user(user)
        except:
            print("Ошибка")

    def subject_and_records(self):
        id = input("Введите ID предмета: ")
        try:
            print(self.subjectController.get_subject_with_records(id))
        except:
            print("Ошибка")


    def run(self):
        while True:
            self.menu()
            choice = input("Выберите действие: ")
            if choice.isdigit() and 1 <= int(choice) <= 5:
                if int(choice) == 1:
                    self.add_user()
                elif int(choice) == 3:
                    self.get_users()
                elif int(choice) == 3:
                    self.get_users()
                elif int(choice) == 17:
                    self.get_users()
                elif int(choice) == 18:
                    self.subject_and_records()
                elif int(choice) == 5:
                    break
            else:
                print("Некорректный ввод.")


def start():
    console = ConsoleApp()
    console.run()

def creation():
    # Based on configuration, use a different database.
    database = SqliteDatabase('librabobus.db')
    # Configure our proxy to use the db we specified in config.
    database_proxy.initialize(database)
    database.drop_tables([UserModelDB, SubjectModelDB, RecordModelDB])
    database.create_tables([UserModelDB, SubjectModelDB, RecordModelDB])


if __name__ == '__main__':
   # creation()
    start()