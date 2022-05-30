class User():
    def __init__(self, name, limit = 1000, id = None):
        self.name = name
        self.limit = limit
        self.id = None

    def change_limit(self, limit):
        self.limit = limit
