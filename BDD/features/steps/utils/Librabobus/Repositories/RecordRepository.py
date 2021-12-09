from ..Entities.Record import Record
from ..Logs.log import logger
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
            logger.info("Record was received")
            return Record(
                    id=record.id,
                    subjectId=record.subjectId,
                    type=record.type,
                    name=record.name,
                    keywords=record.keywords,
                    content=record.content
                )
        except:
            logger.warning("Record wasn't received")
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
        logger.info("Record was received")
        return result

    def findBySubjectId(self, subjectId):
        records = self.RecordModelDB.select().where(RecordModelDB.subjectId == subjectId)
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
        logger.info("Record was received")
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
            logger.info("Record was created")
            return Record(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            )
        except:
            logger.warning("Record wasn't created")
            return None


    def update(self, updateRecord):
        try:
            record = self.RecordModelDB.get(RecordModelDB.id == id)
            record.type = updateRecord.type
            record.name = updateRecord.name
            record.keywords = updateRecord.keywords
            record.content = updateRecord.content
            record.save()
            logger.info("Record was updated")
            return  Record(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            )
        except:
            logger.warning("Record wasn't updated")
            return None

    def delete(self, id):
        try:
            record = self.RecordModelDB.get(RecordModelDB.id == id)
            logger.info("Record was deleted")
            return record.delete_instance()
        except:
            logger.warning("Record wasn't deleted")
            return None