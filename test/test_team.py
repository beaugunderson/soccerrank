from unittest import TestCase
from soccer.team import Team


class TestTeam(TestCase):

    def setUp(self):
        self.obj = Team('Tested')

    def tearDown(self):
        del self.obj

    def test___init__(self):
        self.assertIs('Tested', self.obj.name)

    def test_id(self):
        self.assertEqual('Tested', self.obj.id())

    def test_display(self):
        self.assertEqual('Tested', self.obj.display())
