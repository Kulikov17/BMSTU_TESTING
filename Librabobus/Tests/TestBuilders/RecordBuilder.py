from Librabobus.Entities.Record import Record

class RecordMotherBuilder:
    def init(self, id, subjectId, name):
        self.recordBuilder = RecordBuilder(id, subjectId, name)

    def createRecordLecture(self):
        return self.recordBuilder.withType("Lecture").build()

    def createRecordSeminar(self):
        return self.recordBuilder.withType("Seminar").build()


class RecordBuilder:
    def __init__(self, id, subjectId, name):
        self.id = id
        self.subjectId = subjectId
        self.type = "Lecture"
        self.name = name
        self.keywords = ""
        self.content = ""

    def withType(self, new_type):
        self.type = new_type
        return self

    def withKeyWords(self, new_keywords):
        self.keywords = new_keywords
        return self

    def withContent(self, new_content):
        self.content = new_content
        return self

    def build(self):
        return Record(
            id=self.id,
            subjectId=self.subjectId,
            type=self.type,
            name=self.name,
            keywords=self.keywords,
            content=self.content
        )