from unittest import TestCase

from hurling import Game, Score


class TestGame(TestCase):
    def test_game_creation(self):
        game = Game("Home Team", "Visiting Team")

        self.assertEqual("Home Team", game.home_team)
        self.assertEqual("Visiting Team", game.visiting_team)

        self.assertEqual(Score(0, 0), game.visiting_team_final_score)
        self.assertEqual(Score(0, 0), game.visiting_team_half_time_score)

        self.assertEqual(Score(0, 0), game.home_team_final_score)
        self.assertEqual(Score(0, 0), game.home_team_half_time_score)

        self.assertEqual(1, game.current_half)

        self.assertEqual("Tie", game.winning_team)

    def test_game_halves(self):
        game = Game("Home Team", "Visiting Team")

        self.assertEqual(1, game.current_half)
        game.complete_first_half()
        self.assertEqual(2, game.current_half)
        game.complete_first_half()
        self.assertEqual(2, game.current_half)

    def test_scores(self):
        game = Game("Home Team", "Visiting Team")

        game.add_home_team_goal()
        game.add_home_team_point()

        self.assertEqual(Score(0, 0), game.visiting_team_half_time_score)
        self.assertEqual(Score(0, 0), game.visiting_team_final_score)
        self.assertEqual(Score(1, 1), game.home_team_half_time_score)
        self.assertEqual(Score(1, 1), game.home_team_final_score)
        self.assertEqual(1, game.current_half)
        self.assertEqual("Home Team", game.winning_team)

        game.complete_first_half()
        game.add_visiting_team_goal()
        game.add_visiting_team_point()

        self.assertEqual(Score(0, 0), game.visiting_team_half_time_score)
        self.assertEqual(Score(1, 1), game.visiting_team_final_score)
        self.assertEqual(Score(1, 1), game.home_team_half_time_score)
        self.assertEqual(Score(1, 1), game.home_team_final_score)
        self.assertEqual(2, game.current_half)
        self.assertEqual("Tie", game.winning_team)

        game.add_visiting_team_point()

        self.assertEqual("Visiting Team", game.winning_team)
