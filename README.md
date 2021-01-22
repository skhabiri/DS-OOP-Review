# LSDS Object Oriented Programming Review Assignment

Inside the `football` directory, you will find several files, including a blank `__init__.py`. Don't worry about that one right now. These files together can model several aspects of a football season including a player's statistics, an individual football game, and a season.

As is, these modules are fully functional (well, they run without errors). You can generate a season report by running `season.py`, and you can run the tests using `football_test.py`.

That being said...

Each file (`game.py`, `players.py`, `season.py`, `possible_values.py`, and `football_test.py`) contains at least one `TODO` inside a comment. That is where you can add things and try them out to see if you're understanding how this is all done.

It makes the most sense to begin with `players.py` and `game.py` because they explain the class foundations for the rest of the files (`game.py` more so--since it is used in `season.py`).

To run anything here or in your own, edited version, clone the repo and navigate to the `football` directory in your terminal.
If you would like to run the tests or generate a season report, run `python filename.py` or `python3 filename.py` depending on your configuration with the appropriate choice of `football_test.py` or `season.py`.
If you would like to interactively create instances of the `Player`, `Quarterback`, `Game`, or your own, added, classes and run different methods on them, run `python` or `python3` in terminal and `import` the appropriate module (file name without the `.py`) on the python shell (when you see `>>>`, for example).

___

**OOP-PEP8-312:** 

An example of Animal class in https://github.com/skhabiri/lambdata repo. The python filename is oop_examp.py. It defines a class of Animal and includes the \_\_init__ method to construct the class by receiving the parameters and storing them as an instance field, such as self.name. Other methods in the class gain access to the instance field by passing self as a parameter to them. In calling class_instance.method() we implicitly pass the self to the method and do not need to specify it inside parentheses. Tiger is a subclass of Animal. It overwrites Animal \_\_init__ method as it needs to add more parameters (stripes) to the class. By calling super(). \_\_init__(params), inside Tiger__init__(), self of the Tiger passes to \_\_init__ of super() as a higher scope variable. An example of instantiation:
```
too = Tiger(name="tigi", weight=2000, stripes=100)`
`>>> too.food
'meat'
```
self.name and self.weight are updated through super(). \_\_init__(). self.food takes its value as default in super(). self.stripes is updated byTarget.\_\_init__ method.
Another example of oop about football is in https://github.com/skhabiri/DS-OOP-Review . 


1. game.py 
   1. Class: Game(teams=[team1, team2], score={team1:score1, team2:score2}, locatio, week).
      1. Method: touchdown(self, team, extra_point=1)        # updates the team score
      2. Method: field_goal(self, team)        # updates the team score
      3. Method: safety(self, team)                # updates the team score
      4. Method: get_winning_team(self)        # returns the name of the higher score and lower score teams among the two
2. players.py
   1. Class: Player(name=None, yards=120, touchdowns=5, safety=1, interceptions=0, field_goals=3)
      1. Method: get_points()                # calculate the total points scored from touchdowns and safety
   2. Class: Quarterback(name=None, yards=130, touchdowns=5, completed_passes=20, interceptions=4, safety=None, field_goals=None)
      1. passing_score()                # calculates score based on intercept and completed_passes
   3. Class: Defensive(name=None, yards=130, touchdowns=5, interceptions=4, safety=None, field_goals=None, tackles=2, sacks=3)
3. season.py
   1. Function: generate_rand_games(n=20)        # based on the team names in possible_values.py generate n random instances of Game(), pick pair of random teams and assign random scores. Returns list of games
   2. Function: season_report(games): saves list of winning and losing teams for each game, and saves the total scores of all winning and all losing teams. Saves a dictionary of each team with it’s total scores. Record number of wins and losses for each team in a dictionary. Report each team’s number of wins and lossed, report the average score of a winning/losing team. Report the team with overall highest score as the winner.

### Unit Testing:
For testing the individial methods:
```
cd DS-OOP-Review     # project directory
pipenv shell         # activate virtual environment
python football/football_test.py --verbose      # run the test module from command prompt
```





