# Imports

# Classes
from Make_move import Make_move

# 4 OF 6 CLASSES Pass INHERITS Make_move
# then atemps to pass the ball but the other team may get it
class Pass(Make_move):
    # 2 class attribute
    win = True
    not_injured = True

    def __init__(self, move_making_team, opposing_team):
        # OVERRIDES SUPPERCLASS METHOD
        super().__init__(move_making_team, opposing_team)

    # 1st METHOD MODIFIES CLASS ATTRIBUTE win
    def make_the_move(self):
        win = self.win_or_not()
        not_injured = self.injured_or_not()
        return win and not_injured if True else False

    # 2st METHOD MODIFIES CLASS ATTRIBUTE injured
    def pretend_pass(self):
        win = self.win_or_not()
        not_injured = self.injured_or_not()
        return win and not_injured if True else False