class Team:
    'Team class provides all properties and methods about soccer team'

    def __init__(self, name):
        self.name = name

    def id(self):
        return self.name

    def display(self):
        return self.name
