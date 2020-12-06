# Imports
import random

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
    location = ["SF", 'NYC', 'Miami', 'Denver', 'Dallas Texas']
    

    def __init__(self, team1_name, team2_name):
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.team1 = Team(self.team1_name, random.choice(self.location))
        self.team2 = Team(self.team2_name, random.choice(self.location))
        self.team1_pass = Pass(self.team1_name, self.team2_name)
        self.team2_pass = Pass(self.team2_name, self.team1_name)
        self.team1_shot = Shoot(self.team1_name, self.team2_name)
        self.team2_shot = Shoot(self.team2_name, self.team1_name)

    

    def find_winer(self):
        while(team1_score < 7 or team2_score < 7):
            if team1_turn:
                PassOrShoot = input('Team1 type, "Pass" or "Shoot": ')

                #Check for Player Input
                if PassOrShoot.lower() == "pass":
                    fake_out = input('Team1 pretend to pass? Y or N: ')

                    #Check for Player Input
                    if fake_out.lower() == "y":
                        if self.team1_pass.pretend_pass():
                            self.team2_score -= 1
                            print(f"Wow your pretend pass just made the {self.team2_name} foul! They are down 1 pint!")
                        else:
                            print(f"Hhmmm... Well {self.team1_name}, you were close to making the other team foul but no luck, maybe next time!")
                    else:
                        if self.team1_pass.make_the_move():
                            self.team1.dis_form_hoop -= 1
                else:
                    if self.team1.dis_form_hoop < 3 and team2.pretend_shot() and self.team1_shot():
                        team1_score +=1
                        print(f"{self.team1_name} socer up by 1")
                    else:
                        print(f"OOO almost but not quite {self.team1_name} ")
                        
                team1_turn = False
            else:
                PassOrShoot = input('Team2 type, "Pass" or "Shoot": ')

                #Check for Player Input
                if PassOrShoot.lower() == "pass":
                    fake_out = input('Team2 pretend to pass? Y or N: ')

                    #Check for Player Input
                    if fake_out.lower() == "y":
                        if self.team2_pass.pretend_pass():
                            self.team1_score -= 1
                            print(f"Wow your pretend pass just made the {self.team1_name} foul! They are down 1 pint!")
                        else:
                            print(f"Hhmmm... Well {self.team2_name}, you were close to making the other team foul but no luck, maybe next time!")
                    else:
                        if self.team2_pass.make_the_move():
                            self.team2.dis_form_hoop -= 1
                else:
                    if self.team2.dis_form_hoop < 3 and team1.pretend_shot() and self.team2_shot():
                        team2_score +=1
                        print(f"{self.team2_name} socer up by 1")
                    else:
                        print(f"OOO almost but not quite {self.team2_name} ")
                        
                team2_turn = False

            if team1_score >= 7:
                print(f"{self.team1_name} Wins!")
            else:
                print(f"{self.team2_name} Wins!")

   