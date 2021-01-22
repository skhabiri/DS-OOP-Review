import unittest
from players import Player, Quarterback
from possible_values import *
from game import Game
from season import generate_rand_games

# import the `season` file and make sure generate_random_games only
# makes games with appropriate team names (and never has a team playing itself)


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        """
        Tests field_goal() method of Game class
        """
        game1 = Game(teams=["teamA", "teamB"])
        game1.field_goal("teamA")
        self.assertEqual(game1.score["teamA"], 3)

    def test_get_winnerr(self):
        """
        Tests get_winning_team() method of Game class
        """
        game1 = Game(teams=["teamA", "teamB"])
        game1.field_goal("teamA")
        game1.safety("teamB")
        self.assertTrue(game1.get_winning_team()[0] == "teamA")


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        """
        Uses default values of completed_passes and interceptions
        to calculate the passing score
        """
        qb = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb.passing_score())

class GameGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.league = generate_rand_games(2000)
    
    def test_number_of_games(self):
        self.assertEqual(len(self.league), 2000)

    def test_unique_teams(self):
        """
        Tests if no team plays with itself in generate_rand_games
        """
        for game in self.league:
            self.assertNotEqual(game.teams[0], game.teams[1])

if __name__ == '__main__':
    unittest.main()
