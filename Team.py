# Imports
import random

# Classes
from Player import Player

# 2 OF 6 CLASSES Team builds a women's basketball team
class Team:
    # 1 class attribute
    player_types = ["Center", 'Power Forward', 'Small Forward', 'Point Guard', 'Shooting Guard']
    player_count = 12

    # 4 INIT ATTRIBUTES 
    def __init__(self, team_name, location):
        self.team_name = team_name
        self.location = location
        self.players = []

        # COMPOSITION is used here to create the women players in this basketball team 
        # by INSTANTIATING the player class for each player through a for loop
        for i in range(self.player_count):
            if self.players == []:
                new_player = Player(i, "Center", 0, random.uniform(5000000, 20000000))
                self.players.append(new_player)

            elif hasattr(self.players[i], 'Power Forward'):
                if hasattr(self.players[i], 'Small Forward'):
                    if hasattr(self.players[i], 'Point Guard'):
                        if hasattr(self.players[i], 'Shooting Guard'):
                            new_player = Player(i, random.choice(self.player_types), 0, random.uniform(5000000, 20000000))
                            self.players.append(new_player)
                        else:
                            new_player = Player(i, 'Shooting Guard', 0, random.uniform(5000000, 20000000))
                            self.players.append(new_player)
                    else:
                        new_player = Player(i, 'Point Guard', 0, random.uniform(5000000, 20000000))
                        self.players.append(new_player)
                else:
                    new_player = Player(i, 'Small Forward', 0, random.uniform(5000000, 20000000))
                    self.players.append(new_player)
            else:
                new_player = Player(i, 'Power Forward', 0, random.uniform(5000000, 20000000))
                self.players.append(new_player)