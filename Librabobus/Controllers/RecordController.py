from Librabobus.Services.RecordService import RecordService


class RecordController:
    def __init__(self, url):
        self.recordService = RecordService(url)

    def get_record(self, id):
        try:
            return self.recordService.get_record(id)
        except:
            return None

    def get_records(self):
        try:
            return self.recordService.get_records()
        except:
            return None

    def create_record(self, createRecordDto):
        try:
            return self.recordService.create_record(createRecordDto)
        except:
            return None

    def update_record(self, updateRecordDto):
        try:
            return self.recordService.update_record(updateRecordDto)
        except:
            return None

    def delete_record(self, id):
        try:
            return self.recordService.delete_record(id)
        except:
            None