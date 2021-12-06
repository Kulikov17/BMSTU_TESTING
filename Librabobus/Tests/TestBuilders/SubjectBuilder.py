from Librabobus.Entities.Subject import Subject


class SubjectMotherBuilder:
    def init(self, id, ownerId, name):
        self.subjectBuilder = SubjectBuilder(id, ownerId, name)

    def createPrivateSubject(self):
        return self.subjectBuilder.withPrivate(True).build()

    def createPublicSubject(self):
        return self.subjectBuilder.withPrivate(False).build()



class SubjectBuilder:
    def __init__(self, id, ownerId, name):
        self.id = id
        self.ownerId = ownerId
        self.private = False
        self.name = name
        self.description = ""

    def withPrivate(self, new_private):
        self.private = new_private
        return self

    def withDescription(self, new_description):
        self.description = new_description
        return self

    def build(self):
        return Subject(
            id=self.id,
            ownerId=self.ownerId,
            private=self.private,
            name=self.name,
            description=self.description
        )