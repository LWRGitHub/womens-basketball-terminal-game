# Imports

# Classes
from Play_game import Play_game

if __name__ == "__main__":
    game_is_running = True

    # INSTANTIATES Play_game 
            
    while game_is_running:

    
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Play again
            pass