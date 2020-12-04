# Imports

# Classes
from Team import Team
from Pass import Pass
from Shoot import Shoot

# 1 OF 6 CLASSES Play_game INSTANTIATES Team to set up game 
# Then INSTANTIATES Pass and/or Shoot to play game
class Play_game:

    team1_score = 0
    team2_score = 0
    team1_turn = True
    

    def __init__(self, team1_name, team2_name):
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.team1 = Team(self.team1_name, location)
        self.team2 = Team(self.team2_name, location)
        self.team1_pass = Pass(self.team1_name, self.team2_name)
        self.team2_pass = Pass(self.team2_name, self.team1_name)

    if team1_turn:
        PassOrShoot = input('Team1 type, "Pass" or "Shoot": ')

        #Check for Player Input
        if PassOrShoot.lower() == "pass":
            fake_out = input('Team1 pretend to pass? Y or N: ')

            #Check for Player Input
            if fake_out.lower() == "y":
                if team1_pass.pretend_pass():
                    team2_score -= 1
                    print(f"Wow your pretend pass just made the {self.team2_name} foul! They are down 1 pint!")
    else:

   