# Imports
import string
import random

# Set up 
# makes the "string" import have 
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters

# 3 of 6 classes Player builds each women basketball player
class Player:
    # 1 class attribute
    player_name = ""
    for i in range(int(random.uniform(3, 8))):
        player_name += random.choice(string.ascii_letters)

    # 4 INIT ATTRIBUTES 
    def __init__(self, num, player_type, raise_request_count, annual_income):
        self.num = num
        self.player_type = player_type
        #PROTECTED ATTRIBUTE
        self._raise_request_count = raise_request_count
        #PRIVET ATTRIBUTE
        self.__annual_income = annual_income