from unittest import TestCase
from soccer.team import Team
from soccer.match import Match
from soccer.score import Score


class TestScore(TestCase):

    def setUp(self):
        self.obj = Score()

        self.team_a = Team('A')
        self.team_b = Team('B')
        self.team_c = Team('C')
        self.team_d = Team('D')

    def tearDown(self):
        del self.obj

    def test_add_result(self):
        exp = []
        self.assertEqual(exp, list(self.obj.results.keys()))

        self.helper_add_match(self.team_a, 1, self.team_c, 0)
        exp = ['A', 'C']
        self.assertEqual(exp, list(self.obj.results.keys()))

        self.helper_add_match(self.team_a, 1, self.team_b, 0)
        exp = ['A', 'C', 'B']
        self.assertEqual(exp, list(self.obj.results.keys()))

        self.helper_add_match(self.team_a, 1, self.team_d, 2)
        self.helper_add_match(self.team_b, 0, self.team_d, 2)
        self.helper_add_match(self.team_c, 0, self.team_d, 2)
        exp = ['A', 'C', 'B', 'D']
        self.assertEqual(exp, list(self.obj.results.keys()))

    def test_sort_teams(self):
        exp = []
        self.assertEqual(exp, list(self.obj.sort_teams().keys()))

        self.helper_add_match(self.team_a, 1, self.team_b, 0)
        self.helper_add_match(self.team_a, 1, self.team_c, 0)
        self.helper_add_match(self.team_a, 1, self.team_d, 2)
        exp = ['A', 'D', 'B', 'C']
        self.assertEqual(exp, list(self.obj.sort_teams().keys()))

    def test_display(self):
        exp = ""
        self.assertEqual(exp, self.obj.display())

        self.helper_add_match(self.team_a, 1, self.team_c, 0)
        exp = "1. A, 3 pts\n2. C, 0 pts"
        self.assertEqual(exp, self.obj.display())

        self.helper_add_match(self.team_a, 1, self.team_d, 2)
        self.helper_add_match(self.team_c, 1, self.team_d, 1)
        exp = "1. D, 4 pts\n2. A, 3 pts\n3. C, 1 pt"
        self.assertEqual(exp, self.obj.display())

        self.helper_add_match(self.team_a, 1, self.team_b, 2)
        exp = "1. D, 4 pts\n2. A, 3 pts\n2. B, 3 pts\n4. C, 1 pt"
        self.assertEqual(exp, self.obj.display())

    def test_rank(self):
        lines = []
        exp = ""
        self.assertEqual(exp, Score.rank(lines))

        lines = [
            "Team B 3, Team C 3",
            "Team A 1, Team E 0",
            "Team B 1, Team E 1",
            "Team A 3, Team C 1",
            "Team B 4, Team D 0",
        ]
        exp = "\n".join([
            "1. Team A, 6 pts",
            "2. Team B, 5 pts",
            "3. Team C, 1 pt",
            "3. Team E, 1 pt",
            "5. Team D, 0 pts",
        ])
        self.assertEqual(exp, Score.rank(lines))

    ####
    def helper_add_match(self, t_a: Team, g_a: int, t_b: Team, g_b: int):
        match = Match(t_a, t_b)
        match.add_goals(t_a, g_a)
        match.add_goals(t_b, g_b)
        self.obj.add_result(match)
