from Librabobus.Dtos.SubjectAndRecordDto import SubjectAndRecordsDto
from Librabobus.Dtos.SubjectDto import SubjectDto
from Librabobus.Entities.Record import Record
from Librabobus.Entities.Subject import Subject
from Librabobus.Repositories.RecordRepository import RecordRepository
from Librabobus.Repositories.SubjectRepository import SubjectRepository


class SubjectService:
    def __init__(self, url):
        self.subjectRepository = SubjectRepository(url)
        self.recordRepository = RecordRepository(url)

    def get_subject(self, id):
        subject = self.subjectRepository.findById(id)
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
            return SubjectDto(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            )
        except:
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
            return SubjectDto(
                id=subject.id,
                ownerId=subject.ownerId,
                private=subject.private,
                name=subject.name,
                description=subject.description
            )
        except:
            return None

    def delete_subject(self, id):
        countDelete = self.subjectRepository.delete(id)
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