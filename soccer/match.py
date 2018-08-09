from soccer.team import Team
from typing import Dict


# making this its own method also makes it testable
def score(team_a, team_b):
    if team_a > team_b:
        return (3, 0)

    if team_a == team_b:
        return (1, 1)

    if team_a < team_b:
        return (0, 3)


class Match:

    def __init__(self, team_a: Team, team_b: Team):
        # probably clearer to not use dicts here since soccer matches are
        # always two teams :)
        self.a = team_a
        self.b = team_b

        self.a_goals = 0
        self.b_goals = 0

    def add_goals(self, team: Team, goals: int):
        """
        :param team: instance of the Team class
        :type goals: number of goals (integer)
        """
        if team.id() == self.a.id():
            self.a_goals += goals
        elif team.id() == self.b.id():
            self.b_goals += goals
        else:
            raise Exception(f'Unexpected team: "{team.id()}"')

    def goals(self, team_id):
        if team_id == self.a.id():
            return self.a_goals

        if team_id == self.b.id():
            return self.b_goals

        raise Exception(f'Unexpected team: "{team_id}"')

    def team(self, team_id: str) -> Team:
        # .get() takes a default for if the requested key is not found
        # but if requested team is not found I think it may be better to throw
        # here?
        #
        # try:
        #     return self.teams[team_id]
        # except KeyError:
        #     raise Exception(f'Team not found: "{team_id}"')
        #
        # but since we can get away without using a dict:
        if team_id == self.a.id():
            return self.a

        if team_id == self.b.id():
            return self.b

        raise Exception(f'Unexpected team: "{team_id}"')

    def points(self) -> Dict:
        # rewritten for clarity
        a_points, b_points = score(self.goals(self.a.id()),
                                   self.goals(self.b.id()))

        return {
            self.a.id(): a_points,
            self.b.id(): b_points,
        }
