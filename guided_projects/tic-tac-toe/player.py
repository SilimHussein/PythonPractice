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

# Player that inputs moves manually ( a human)
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
        
# Unbeatable computer player (smart computer)
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # Get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # First we want to check if the previous move is a winner
        # This is our base case
        if state.current_winner == other_player:
            # We should return position and score to keep track of the score for minimax to work
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() +1) if other_player == max_player 
                        else -1 * (state.num_empty_squares()+1)
                }
        elif not state.empty_squares(): # No empty squares
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # Each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} # Each score should minimize. so we initialize to the highest posible number.

        for possible_move in state.available_moves():

            # Step 1: make a move, try that spot
            state.make_move(possible_move, player)
            
            # Step 2: recurse using minimax to simulate game after making that move
            sim_score = self.minimax(state, other_player) # Now, we alternate players

            # Step 3: Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # set the position we have moved to, or it will mess recursion part

            # Step 4: update the diictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best