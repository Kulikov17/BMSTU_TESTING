class SubjectDto:
    def __init__(self, id, ownerId, private, name, description):
        self.id = id
        self.ownerId = ownerId
        self.private = private
        self.name = name
        self.description = description

class CreateSubjectDto:
    def __init__(self, ownerId, private, name, description):
        self.ownerId = ownerId
        self.private = private
        self.name = name
        self.description = description