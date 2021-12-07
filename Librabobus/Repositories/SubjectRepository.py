from ..Entities.Subject import Subject
from ..Logs.log import logger
from ..Models.Subject import SubjectModelDB
from ..db_settings import database_proxy, database_connect


class SubjectRepository:
    def __init__(self, url):
        # Based on configuration, use a different database.
        self.database = database_connect(url)
        # Configure our proxy to use the db we specified in config.
        database_proxy.initialize(self.database)
        self.SubjectModelDB = SubjectModelDB

    def findById(self, id):
        try:
            subject = self.SubjectModelDB.get(SubjectModelDB.id == id)
            logger.info("Subject was received")
            return Subject(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            )
        except:
            logger.warning("Subject wasn't received")
            return None


    def findAll(self):
        subjects = self.SubjectModelDB.select()
        result = []
        for subject in subjects:
            result.append(Subject(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            ))
        logger.info("Subject was received")
        return result


    def create(self, newSubject):
        try:
            subject = self.SubjectModelDB(
                ownerId=newSubject.ownerId,
                private=newSubject.private,
                name=newSubject.name,
                description=newSubject.description
            )
            subject.save()
            logger.info("Subject was created")
            return Subject(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            )
        except:
            logger.warning("Subject wasn't created")
            return None


    def update(self, updateSubject):
        try:
            subject = self.SubjectModelDB.get(SubjectModelDB.id == id)
            subject.private = updateSubject.private,
            subject.name = updateSubject.name,
            subject.description = updateSubject.description
            subject.save()
            logger.info("Subject was updated")
            return Subject(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            )
        except:
            logger.warning("Subject wasn't updated")
            return None

    def delete(self, id):
        try:
            subject = self.SubjectModelDB.get(SubjectModelDB.id == id)
            logger.info("Subject was deleted")
            return subject.delete_instance()
        except:
            logger.warning("Subject wasn't deleted")
            return None

    def findByOwnerId(self, ownerId):
        subjects = self.SubjectModelDB.select().where(SubjectModelDB.ownerId == ownerId)
        result = []
        for subject in subjects:
            result.append(Subject(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            ))
        logger.info("Subject was received")
        return result