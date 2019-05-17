from unittest import TestCase

from scoreboard.hurling import Score


class TestScore(TestCase):
    def test_score_creation(self):
        score = Score()

        self.assertScore(0, 0, score)

    def test_score_creation_with_initial_values(self):
        score = Score(2, 5)

        self.assertScore(2, 5, score)

    def test_goal_and_point_addition(self):
        score = Score()

        score.add_goal()
        score.add_goal()
        score.add_point()
        score.add_point()
        score.add_point()

        self.assertScore(2, 3, score)

    def test_score_addition(self):
        score1 = Score(1, 3)
        score2 = Score(2, 1)

        score_final = score1 + score2

        self.assertScore(3, 4, score_final)

    def test_equality_equals(self):
        score1 = Score(1, 3)
        score2 = Score(1, 3)

        self.assertEqual(score1, score2)

    def test_equality_not_equals(self):
        score1 = Score(2, 3)
        score2 = Score(1, 4)

        self.assertNotEqual(score1, score2)

    def assertScore(self, goals, points, score):
        self.assertEqual(goals, score.goals)
        self.assertEqual(points, score.points)
        self.assertEqual(points + goals * 3, score.total_score)
