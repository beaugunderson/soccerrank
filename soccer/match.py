from soccer.team import Team
from typing import Dict


class Match:

    def __init__(self, team_a: Team, team_b: Team):
        self.teams = {
            team_a.id(): team_a,
            team_b.id(): team_b
        }
        self.goals = {
            team_a.id(): 0,
            team_b.id(): 0
        }

    def add_goals(self, team: Team, goals: int):
        """
        :param team: instance of the Team class
        :type goals: number of goals (integer)
        """
        if team.id() in self.goals:
            self.goals[team.id()] += goals

    def team(self, team_id: str) -> Team:
        return self.teams[team_id] if team_id in self.teams else Team('')

    def points(self) -> Dict:
        points = {}
        # tie by default
        for key in self.goals:
            points.update({key: 1})
        g_max = max(self.goals.values())
        g_min = min(self.goals.values())
        if g_min != g_max:
            for team_id, goals in self.goals.items():
                points[team_id] = 3 if goals == g_max else 0

        return points
