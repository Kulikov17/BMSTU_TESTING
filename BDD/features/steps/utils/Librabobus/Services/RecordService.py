from utils.Librabobus.Dtos.RecordDto import RecordDto
from utils.Librabobus.Entities.Record import Record
from utils.Librabobus.Repositories.RecordRepository import RecordRepository


class RecordService:
    def __init__(self, url):
        self.recordRepository = RecordRepository(url)

    def get_record(self, id):
        record = self.recordRepository.findById(id)
        return RecordDto(
            id=record.id,
            subjectId=record.subjectId,
            type=record.type,
            name=record.name,
            keywords=record.keywords,
            content=record.content
        )

    def get_records_by_subjectId(self, subjectId):
        records = self.recordRepository.findBySubjectId(subjectId)
        result = []
        for record in records:
            result.append(RecordDto(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            ))
        return result


    def get_records(self):
        records = self.recordRepository.findAll()
        result = []
        for record in records:
            result.append(RecordDto(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            ))
        return result

    def create_record(self, createRecordDto):
        newRecord = Record(
            subjectId=createRecordDto.subjectId,
            type=createRecordDto.type,
            name=createRecordDto.name,
            keywords=createRecordDto.keywords,
            content=createRecordDto.content
        )
        try:
            record = self.recordRepository.create(newRecord)
            return RecordDto(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            )
        except:
            return None

    def update_record(self, updateRecordDto):
        updateRecord = Record(
            id=updateRecordDto.id,
            subjectId=updateRecordDto.subjectId,
            type=updateRecordDto.type,
            name=updateRecordDto.name,
            keywords=updateRecordDto.keywords,
            content=updateRecordDto.content
        )
        try:
            record = self.recordRepository.update(updateRecord)
            return RecordDto(
                id=record.id,
                subjectId=record.subjectId,
                type=record.type,
                name=record.name,
                keywords=record.keywords,
                content=record.content
            )
        except:
            return None

    def delete_record(self, id):
        countDelete = self.recordRepository.delete(id)
        return countDelete