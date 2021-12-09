from utils.Librabobus.Services.RecordService import RecordService
from utils.Librabobus.Logs.log import logger

class RecordController:
    def __init__(self, url):
        self.recordService = RecordService(url)

    def get_record(self, id):
        try:
            logger.info("Record was received")
            return self.recordService.get_record(id)
        except:
            logger.warning("Record wasn't received")
            return None

    def get_records(self):
        try:
            logger.info("Records was received")
            return self.recordService.get_records()
        except:
            logger.warning("Records wasn't received")
            return None

    def get_records_by_subject_id(self, subjectId):
        try:
            logger.info("Record was received")
            return self.recordService.get_records_by_subjectId(subjectId)
        except:
            logger.warning("Record wasn't received")
            return None

    def create_record(self, createRecordDto):
        try:
            logger.info("Record was created")
            return self.recordService.create_record(createRecordDto)
        except:
            logger.warning("Record wasn't created")
            return None

    def update_record(self, updateRecordDto):
        try:
            logger.info("Record was updated")
            return self.recordService.update_record(updateRecordDto)
        except:
            logger.warning("Record wasn't updated")
            return None

    def delete_record(self, id):
        try:
            logger.info("Record was deleted")
            return self.recordService.delete_record(id)
        except:
            logger.warning("Record wasn't deleted")
            None