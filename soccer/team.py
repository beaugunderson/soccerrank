# classes like this are a great use case for either namedtuples or the new
# dataclasses
class Team:
    'Team class provides all properties and methods about soccer team'

    def __init__(self, name):
        self.name = name

    # these could use the @property decorator since they're simple
    def id(self):
        return self.name

    def display(self):
        return self.name
