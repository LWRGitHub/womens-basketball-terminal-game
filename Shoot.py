# Imports

# Classes
from Make_move import Make_move

# 5 OF 6 CLASSES Shoot INHERITS Make_move
# then attempts to make a shot but may lose the ball to the other team
class Shoot(Make_move):
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
    def pretend_shot(self):
        win = self.win_or_not()
        not_injured = self.injured_or_not()
        return win and not_injured if False else True

    