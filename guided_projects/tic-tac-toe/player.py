import math
import random

# Base class for any kind of player (human or computer)
class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # This is placeholder method ot be defined in subclasses
    def get_move(self, game):
        pass

# Player that chooses moves randomly (the computer)
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        # Initialize parent class with letter(X or O)
        super().__init__(letter)

    def get_move(self, game):
        # Pick a random square from available moves
        square = random.choice(game.available_moves())
        return square 

# Player taht inputs moves manually ( a human)
class HumanPlayer(Player):
    def __init__(self, letter):
        # Initialize parent class with letter (X or O)
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False # We want to loop until the player pics a valid square
        val = None
        while not valid_square:
            # Ask the player where to move
            square = input(self.letter + "\'s turn. Input move (0-9):")
            try:
                # Convert input into an integer
                val = int(square)
                # Check if the square is a valid move
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then Yay!
            except ValueError:
                # If input is bad or move is not available, ask again
                print("Invalid square. Try again")
            
        return val # Return the valid move to the game.
        