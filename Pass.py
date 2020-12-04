# Imports

# Classes
from Make_move import Make_move

# 4 OF 6 CLASSES Pass INHERITS Make_move
# then atemps to pass the ball but the other team may get it
class Pass(Make_move):

    def __init__(self, move_making_team, opposing_team):
        # OVERRIDES SUPPERCLASS METHOD
        super().__init__(move_making_team, opposing_team)

    def make_the_move(self):
        return self.win_or_not() and self.injured_or_not() if True else False

    def pretend_pass(self):
        return self.win_or_not() and self.injured_or_not() if True else False