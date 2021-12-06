class Subject:
    def __init__(self, id=None, ownerId='', private=False, name='', description=''):
        self.id = id
        self.ownerId = ownerId
        self.private = private
        self.name = name
        self.description = description