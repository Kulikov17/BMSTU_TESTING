class RecordDto:
    def __init__(self, id, subjectId, type, name, keywords, content):
        self.id = id
        self.subjectId = subjectId
        self.type = type
        self.name = name
        self.keywords = keywords
        self.content = content


class CreateRecordDto:
    def __init__(self, subjectId, type, name, keywords, content):
        self.subjectId = subjectId
        self.type = type
        self.name = name
        self.keywords = keywords
        self.content = content