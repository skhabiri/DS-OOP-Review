'''Player class to record stats for individual players
'''


class Player:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.touchdowns
        safety_points = 2 * self.safety
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name, yards, touchdowns,
                         safety, interceptions, field_goals)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score


class Defensive(Player):
    '''defensive is a subclass of player with extra attributes
    '''

    def __init__(self, name=None, yards=130, touchdowns=5,
                 interceptions=4, safety=None, field_goals=None, tackles=2, sacks=3):
        super().__init__(name, yards, touchdowns,
                         safety, interceptions, field_goals)
        self.tackles = tackles
        self.sacks = sacks

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.
