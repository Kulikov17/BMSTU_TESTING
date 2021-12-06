from Librabobus.Services.SubjectService import SubjectService


class SubjectController:
    def __init__(self, url):
        self.subjectService = SubjectService(url)

    def get_subject(self, id):
        try:
            return self.subjectService.get_subject(id)
        except:
            return None

    def get_subjects(self):
        try:
            return self.subjectService.get_subjects()
        except:
            return None

    def create_subject(self, createSubjectDto):
        try:
            return self.subjectService.create_subject(createSubjectDto)
        except:
            return None

    def update_subject(self, updateSubjectDto):
        try:
            return self.subjectService.update_subject(updateSubjectDto)
        except:
            return None

    def delete_subject(self, id):
        try:
            return self.subjectService.delete_subject(id)
        except:
            None

    def create_subject_with_records(self, newSubjectAndRecordDto):
        try:
            return self.subjectService.create_subject_and_record(newSubjectAndRecordDto)
        except:
            None

    def get_subject_with_records(self, id):
        try:
            return self.subjectService.getSubjectWithRecords(id)
        except:
            None