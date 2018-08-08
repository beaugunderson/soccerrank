from unittest import TestCase
from soccer.team import Team
from soccer.match import Match


class TestMatch(TestCase):

    def setUp(self):
        self.team_a = Team('A')
        self.team_b = Team('B')
        self.obj = Match(self.team_a, self.team_b)

    def tearDown(self):
        del self.obj
        del self.team_a
        del self.team_b

    def test___init__(self):
        # initial reference to the teams
        self.assertIs(self.team_a, self.obj.teams['A'])
        self.assertIs(self.team_b, self.obj.teams['B'])

        # initial goals set to 0
        self.assertEqual(0, self.obj.goals['A'])
        self.assertEqual(0, self.obj.goals['B'])

    def test_add_goals(self):
        # initial goals set to 0
        self.assertEqual(0, self.obj.goals['A'])
        self.assertEqual(0, self.obj.goals['B'])

        # add 1 goal to A
        self.obj.add_goals(self.team_a, 1)
        self.assertEqual(1, self.obj.goals['A'])
        self.assertEqual(0, self.obj.goals['B'])

        # add 2 goals to B
        self.obj.add_goals(self.team_b, 2)
        self.assertEqual(1, self.obj.goals['A'])
        self.assertEqual(2, self.obj.goals['B'])

    def test_team(self):
        self.assertIs(self.team_a, self.obj.team('A'))
        self.assertIs(self.team_b, self.obj.team('B'))
        self.assertIsNot(self.team_a, self.obj.team('C'))
        self.assertIsNot(self.team_b, self.obj.team('C'))
        self.assertIsInstance(self.obj.team('C'), Team)

    def test_points(self):
        # not goals --> tie
        exp = {'A': 1, 'B': 1}
        self.assertDictEqual(exp, self.obj.points())

        # A has more goals
        self.obj.add_goals(self.team_a, 2)
        exp = {'A': 3, 'B': 0}
        self.assertDictEqual(exp, self.obj.points())

        # B has more goals
        self.obj.add_goals(self.team_b, 3)
        exp = {'A': 0, 'B': 3}
        self.assertDictEqual(exp, self.obj.points())

        # even goals
        self.obj.add_goals(self.team_a, 1)
        exp = {'A': 1, 'B': 1}
        self.assertDictEqual(exp, self.obj.points())
