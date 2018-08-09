from soccer.match import Match
from soccer.team import Team
from typing import Dict, List
import re


class Score:
    ID = 'id'
    LABEL = 'lb'
    POINT = 'pt'

    def __init__(self):
        self.results = {}
        self.teams = {}

    def add_result(self, match: Match):
        for team_id, points in match.points().items():
            if team_id not in self.results:
                self.results.update({
                    team_id: {
                        self.ID: team_id,
                        self.LABEL: match.team(team_id).display(),
                        self.POINT: 0
                    }
                })
            self.results[team_id][self.POINT] += points

    def sort_teams(self) -> Dict:
        # the info parameter is a list with the key at index 0 and the value at index 1
        # order is reverse for the points and then alphabetical for the name
        res = {}
        for k, i in sorted(self.results.items(), key=lambda info: (-1 * info[1][self.POINT], info[1][self.LABEL])):
            res.update({k: i})
        return res

    def display(self) -> str:
        res = []
        idx = 0
        rnk = 0
        pnt = -1
        for k, v in self.sort_teams().items():
            idx += 1
            if pnt != v[self.POINT]:
                rnk = idx
                pnt = v[self.POINT]
            end = '' if pnt == 1 else 's'
            res.append("%d. %s, %d pt%s" % (rnk, v[self.LABEL], pnt, end))
        return "\n".join(res)

    @staticmethod
    def rank(lines: List) -> str:
        score = Score()
        reg_def = re.compile(r'^(.+) (\d+), (.+) (\d+)$')
        for result in lines:
            reg_res = reg_def.match(result)
            if reg_res:
                team_a = Team(reg_res.group(1))
                team_b = Team(reg_res.group(3))
                match = Match(team_a, team_b)
                match.add_goals(team_a, int(reg_res.group(2)))
                match.add_goals(team_b, int(reg_res.group(4)))
                score.add_result(match)
        return score.display()
