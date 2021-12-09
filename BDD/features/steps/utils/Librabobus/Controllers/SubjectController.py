from utils.Librabobus.Services.SubjectService import SubjectService
from utils.Librabobus.Logs.log import logger

class SubjectController:
    def __init__(self, url):
        self.subjectService = SubjectService(url)

    def get_subject(self, id):
        try:
            logger.info("Subject was received")
            return self.subjectService.get_subject(id)
        except:
            logger.warning("Subject wasn't received")
            return None

    def get_subjects(self):
        try:
            logger.info("Subjects was received")
            return self.subjectService.get_subjects()
        except:
            logger.warning("Subjects wasn't received")
            return None

    def get_subjects_by_owner_id(self, ownerId):
        try:
            logger.info("Subject was received")
            return self.subjectService.get_subjects_by_ownerId(ownerId)
        except:
            logger.warning("Subject wasn't received")
            return None

    def create_subject(self, createSubjectDto):
        try:
            logger.info("Subject was created")
            return self.subjectService.create_subject(createSubjectDto)
        except:
            logger.warning("Subject wasn't created")
            return None

    def update_subject(self, updateSubjectDto):
        try:
            logger.info("Subject was updated")
            return self.subjectService.update_subject(updateSubjectDto)
        except:
            logger.warning("Subject wasn't updated")
            return None

    def delete_subject(self, id):
        try:
            logger.info("Subject was deleted")
            return self.subjectService.delete_subject(id)
        except:
            logger.warning("Subject wasn't deleted")
            None

    def create_subject_with_records(self, newSubjectAndRecordDto):
        try:
            logger.info("Subject was received")
            return self.subjectService.create_subject_and_record(newSubjectAndRecordDto)
        except:
            logger.warning("Subject wasn't received")
            None

    def get_subject_with_records(self, id):
        try:
            logger.info("Subject was received")
            return self.subjectService.getSubjectWithRecords(id)
        except:
            logger.warning("Subject wasn't received")
            None