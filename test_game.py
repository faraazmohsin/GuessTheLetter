from unittest import TestCase


class Test_game(TestCase):
    def test_game_diff(self, difficulty=None):
        self.assertTrue(difficulty == "easy")


class Test_check_letter(TestCase):
    def test_check_letter(self):
        self.assertTrue(3, "p")
