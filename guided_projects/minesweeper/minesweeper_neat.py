import random
import re

# We start by creating a board object to represent minesweeper game
class Board:
    # creates a board and plant bombs
    def __init__(self, dim_size, num_bombs):
        # dimension size and number of bombs comes as an object of the board
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # creating a new board. The helper function creates a new board and plants bombs
        self.board = self.make_new_board()

        # check out how many bombs are surrounding a square
        self.assign_values_to_board()

        # keep track of where we have dug 
        self.dug = set()

    # Helper function to make a new board and plant bombs
    def make_new_board(self):
        # make new board - list of lists, with none as values
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # choose a random interger from anywhere within the boards dimension
            loc = random.randint(0, self.dim_size**2 - 1)
            # change this location into row and col
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            # dont overwrite planted bombs, skip it
            if board[row][col] == "*":
                continue

            # Plant the bombs, increment the values and return the board
            board[row][col] = "*"
            bombs_planted += 1

        return board

    # Helper function to check out how many bombs are surrounding a square
    def assign_values_to_board(self):
        # iterate through row and column
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # if this is already a bomb dont calculate
                if self.board[r][c] == '*':
                    continue
                # calculate how many bombs surrounds a square- using a helper function
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)
    
    # Calculate neighbouring bombs - this function is called from the previous one(also helper)
    def get_num_neighbouring_bombs(self, row, col):
        # we start counting bombs from 0
        num_neighbouring_bombs = 0
        # iterate through rows and columns, using max, min to make sure we dont get out of bounds
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                # this is our original location, we dont track how many bombs are surrouding it.
                if r == row and c == col:
                    continue
                # however, if not our original location, we track- increment it and return it
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
        return num_neighbouring_bombs

    # Helper function to dig at a location, return true if successful, false, if we dug a bomb
    def dig(self, row, col):
        # Keep a track that we dug here
        self.dug.add((row, col))

        # Scenario 1: if we dug a bomb - return false(game over)
        if self.board[row][col] == '*':
            return False
        # Scenario 2: if we didnt dig a bomb - retrun True
        elif self.board[row][col] > 0:
            return True
        # Scenario 3: if we dug a place without neighbouring bomb, dig recursively until you get a bomb
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
             for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return  True

    # Magic function for printing this object
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                # if we have already dug a square successfully. show how many bombs surrounds it.
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                # if w havent dug, show empty spaces
                else:
                    visible_board[row][col] = ' '

        # Formatting stuff...
        # put this together in a string
        string_rep = ''
        # get max column widths for printing 
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
        

# Play the game
def play(dim_size=10, num_bombs=10):
    # step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    safe = 0

    # step 2: show the user the board and ask where they want to dig
    while len(board.dug) < dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where do you want to dig?, format = row, col :"))
        # We need to check for invalid location, if the user inputs a digit that is out of bounds
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print('Invalid  input, try again')
            continue
        # step 3: if location is a bomb, end the loop, game over, if not, dig recursively until we get neighbouring bomb_num
        # if valid we dig recursively
        safe = board.dig(row, col)
        # if not safe, game over
        if not safe:
            break
        
        # two ways to end the loop
    if safe:
        print('You are victorious !')
    else:
        print('You lost, game over, try again another time')
        # reveal the board with the bombs
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()

