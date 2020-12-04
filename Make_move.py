# Imports
import random

# 6 OF 6 CLASSES Make_move is the class the will get 
# INHERITED by Pass & Shoot inorder to make the move
class Make_move:
    win = True
    not_injured = True

    # 2 INIT ATTRIBUTES 
    def __init__(self, move_making_team, opposing_team):
        self.move_making_team = move_making_team
        self.opposing_team = opposing_team

    # 1st METHOD MODIFIES CLASS ATTRIBUTE win
    def win_or_not(self):
        if random.uniform(1, 11) % 2 != 0:
            self.win = False

        return self.win

    # 2nd METHOD MODIFIES CLASS ATTRIBUTE injured
    def injured_or_not(self):
        if random.choice([2,2,2,2,2,1,2,2,2,1]) % 2 != 0:
            self.not_injured = False

        return self.not_injured