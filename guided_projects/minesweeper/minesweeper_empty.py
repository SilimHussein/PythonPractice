import random 
import re
# Creating a board object to represent the minesweeper board
# This is so that we when we code up the game, we can just say create a "new board object"
# and dig on that board etc.
class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of thse parameters because we might find them helpful later on
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Get the board
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # Initialize a set to keep track of which locations we have uncovered
        # We will put (row, col) tuples into these sets
        self.dug = set()

    def make_new_board(self):
        # Construct a new board based on the dim size and num bombs
        # We should construct the list of lists here( or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is more natural)
        return [] # change this

    def assign_values_to_board(self):
        # Now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighbouring bombs there are. We can precompute these and it'll save us some
        # effort checking whats around the board later on :)
        pass

    def get_num_neighbouring_bombs(self, row, col):
        # Let's iterate through each of the neighbouring positions and sum the number of bombs
        # Top left: (row-1, col-1)
        # Top middle: (row-1, col)
        # Top right: (row-1, col+1)
        # Left: (row, col-1)
        # Right: (row, col+1)
        # Bottom left: (row+1, col-1)
        # Bottom middle: (row+1, col)
        # Bottom rightL (row+1, col+1)

        # ps we need to make sure we dont go out of bounds!! 
        pass

    def dig(self, row, col):
        # Dig at that location! 
        # REturn True if successful dig, Falase if bomb dug

        # A couple of scenarios to consider:
        # Hit a bomb -> game over
        # Dig at a location with neighbouring bombs -> finish dig
        # Dig at a location with  no neighbouring bombs -? recursively dig neighbour!
        pass

    def __str__(self):
        # Return a string that shows the board to the player
        # Note: this part is kinda hard toget the formmating right, you dont have to  do it the same way I did
        # You can also just copy and paste from the implementation
        # This part is not that important to understanding the logic of the the code :)
        return ''

    def pay(dim_size=10, num_bombs=10):
        # Step 1: create the board and plant the bombs
        # Step 2: show the user the board and ask for where they want to dig
        # Step 3a: if the location is a bomb, then show the game over message
        # Step 3b, if the location is not a bomb, dig recursively until one of the squares is next to a bomb
        # Step 4: repeat steps 2 and 3 until there are no more places to dig, the show victory.
        pass
    
    if __name__='__main__':
        play()