from Librabobus.Dtos.SubjectAndRecordDto import SubjectAndRecordsDto
from Librabobus.Dtos.SubjectDto import SubjectDto
from Librabobus.Entities.Record import Record
from Librabobus.Entities.Subject import Subject
from Librabobus.Logs.log import logger
from Librabobus.Repositories.RecordRepository import RecordRepository
from Librabobus.Repositories.SubjectRepository import SubjectRepository


class SubjectService:
    def __init__(self, url):

        self.subjectRepository = SubjectRepository(url)
        self.recordRepository = RecordRepository(url)

    def get_subject(self, id):
        subject = self.subjectRepository.findById(id)
        logger.info("Subject was received")
        return SubjectDto(
            id=subject.id,
            ownerId=subject.ownerId,
            private=subject.private,
            name=subject.name,
            description=subject.description
        )

    def get_subjects(self):
        subjects = self.subjectRepository.findAll()
        result = []
        for subject in subjects:
            result.append(SubjectDto(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            ))
        logger.info("Subject was received")
        return result

    def get_subjects_by_ownerId(self, ownerId):
        subjects = self.subjectRepository.findByOwnerId(ownerId)
        result = []
        for subject in subjects:
            result.append(SubjectDto(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            ))
        logger.info("Subject was received")
        return result

    def create_subject(self, createSubjectDto):
        newSubject = Subject(
            ownerId=createSubjectDto.ownerId,
            private=createSubjectDto.private,
            name=createSubjectDto.name,
            description=createSubjectDto.description
        )
        try:
            subject = self.subjectRepository.create(newSubject)
            logger.info("Subject was created")
            return SubjectDto(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            )
        except:
            logger.warning("Subject wasn't created")
            return None

    def update_subject(self, updateSubjectDto):
        updateSubject = Subject(
            id=updateSubjectDto.id,
            ownerId=updateSubjectDto.ownerId,
            private=updateSubjectDto.private,
            name=updateSubjectDto.name,
            description=updateSubjectDto.description
        )
        try:
            subject = self.subjectRepository.update(updateSubject)
            logger.info("Subject was updated")
            return SubjectDto(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            )
        except:
            logger.warning("Subject wasn't updated")
            return None

    def delete_subject(self, id):
        countDelete = self.subjectRepository.delete(id)
        logger.info("Subject was deleted")
        return countDelete

    def create_subject_and_record(self, newSubjectAndRecordDto):
        try:
            newSubject = Subject(
                ownerId=newSubjectAndRecordDto.ownerId,
                private=newSubjectAndRecordDto.private,
                name=newSubjectAndRecordDto.name,
                description=newSubjectAndRecordDto.description
            )
            subject = self.subjectRepository.create(newSubject)

            newRecord = Record(
                subjectId=subject.id,
                type=newSubjectAndRecordDto.type,
                name=newSubjectAndRecordDto.name,
                keywords=newSubjectAndRecordDto.keywords,
                content=newSubjectAndRecordDto.content
            )

            record = self.subjectRepository.create(newRecord)
            return True
        except:
            return False

    def getSubjectWithRecords(self, id):
        try:
            subject = self.subjectRepository.findById(id)
            records = self.recordRepository.findBySubjectId(subject.id)

            return SubjectAndRecordsDto(
                ownerId = subject.ownerId,
                private = subject.private,
                name = subject.name,
                description = subject.description,
                records = records
            )
        except:
            return None