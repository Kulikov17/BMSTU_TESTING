from peewee import SqliteDatabase

from ..Entities.Record import Record
from ..Models.Record import RecordModelDB
from ..db_settings import database_proxy, database_connect


class RecordRepository:
    def __init__(self, url):
        # Based on configuration, use a different database.
        self.database = database_connect(url)
        # Configure our proxy to use the db we specified in config.
        database_proxy.initialize(self.database)
        self.RecordModelDB = RecordModelDB

    def findById(self, id):
        try:
            record = self.RecordModelDB.get(RecordModelDB.id == id)
            return Record(
                    id=record.id,
                    subjectId=record.subjectId,
                    type=record.type,
                    name=record.name,
                    keywords=record.keywords,
                    content=record.content
                )
        except:
            return None


    def findAll(self):
        records = self.RecordModelDB.select()
        result = []
        for record in records:
            result.append(Record(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            ))
        return result

    def findBySubjectId(self, subjectId):
        records = self.RecordModelDB.select().where(RecordModelDB.ownerId == subjectId)
        result = []
        for record in records:
            result.append(Record(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            ))
        return result

    def create(self, newRecord):
        try:
            record = self.RecordModelDB(
                subjectId=newRecord.subjectId,
                type=newRecord.type,
                name=newRecord.name,
                keywords=newRecord.keywords,
                content=newRecord.content
            )
            record.save()
            return Record(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            )
        except:
            return None


    def update(self, updateRecord):
        try:
            record = self.RecordModelDB.get(RecordModelDB.id == id)
            record.type = updateRecord.type
            record.name = updateRecord.name
            record.keywords = updateRecord.keywords
            record.content = updateRecord.content
            record.save()
            return  Record(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            )
        except:
            return None

    def delete(self, id):
        try:
            record = self.RecordModelDB.get(RecordModelDB.id == id)
            return record.delete_instance()
        except:
            return None