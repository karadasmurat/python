from unittest import TestCase
from day04_rock_paper_scissors import check_first_wins

class TestWinner(TestCase):

    # test method starts with test_
    def test_draw(self):
        self.assertEqual(check_first_wins('r', 'r'), "draw")
        self.assertEqual(check_first_wins('p', 'p'), "draw")
        self.assertEqual(check_first_wins('s', 's'), "draw")

    def test_win(self):
        self.assertEqual(check_first_wins('r', 's'), "win")
        self.assertEqual(check_first_wins('p', 'r'), "win")
        self.assertEqual(check_first_wins('s', 'p'), "win")

    def test_loose(self):
        self.assertEqual(check_first_wins('r', 'p'), "loose")
        self.assertEqual(check_first_wins('p', 's'), "loose")
        self.assertEqual(check_first_wins('s', 'r'), "loose")
