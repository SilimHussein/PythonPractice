import math
import random

class Player:
    def _init_(self, letter):
        # letter is x or o
        self.letter = letter

    #we want all players to get their move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self, game):
        random.choice(game.available_moves())
        return square 

class HumanPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-9):")
            # we are going to check that this is a correct value by tryint cast it into an integer
            # and if its not, then we say its invalid, if that spot is not available on the board, 
            # we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves:
                    raise ValueError
                valid_square = True # if these are successful, then Yay!
            except ValueError:
                print("Invalid square. Try again")
            
        return val
        