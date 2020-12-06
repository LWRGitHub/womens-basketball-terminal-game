# Imports

# Classes
from Play_game import Play_game

if __name__ == "__main__":
    game_is_running = True

    while game_is_running:
        print("Wellcome to The Women's Backetball Game!")

        team1 = input("Team 1 name: ")
        team2 = input("Team 2 name: ")

        # INSTANTIATES Play_game 
        game = Play_game(team1, team2)
        game.find_winer()


    
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False