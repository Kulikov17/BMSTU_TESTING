import unittest

from peewee import SqliteDatabase

from Librabobus.Controllers.RecordController import RecordController
from Librabobus.Controllers.SubjectController import SubjectController
from Librabobus.Controllers.UserController import UserController
from Librabobus.Models.Record import RecordModelDB
from Librabobus.Models.Subject import SubjectModelDB
from Librabobus.Models.User import UserModelDB
from Librabobus.db_settings import database_proxy
from Librabobus.librabobus import ConsoleApp


class workAll(unittest.TestCase):
    def test_create_record(self):
        self.console.get_user()

    def setUp(self):
        url = 'testlibrabobus.db'
        creation_mock(url)
        self.console = ConsoleApp(url)


def creation_mock(url):
    database = SqliteDatabase(url)
    database_proxy.initialize(database)
    database.drop_tables([UserModelDB, SubjectModelDB, RecordModelDB])
    database.create_tables([UserModelDB, SubjectModelDB, RecordModelDB])


if __name__ == '__main__':
    unittest.main()
