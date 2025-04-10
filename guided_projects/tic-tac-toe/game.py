from player import HumanPlayer, RandomComputerPlayer
import random
import time

# Function to show emoji fireworks when someone wins
def print_emoji_fireworks():
    fireworks = ['🎆', '🎇', '✨', '🚀', '🔥', '🌟']
    for _ in range(5):
        line = '   '.join(random.choices(fireworks, k=10))
        print(line)
        time.sleep(0.3)
    print("\n")

# Game class that control the board, rules and winner logic
class TicTacToe:
    def __init__(self):
        # Start with an empty board (9 spaces)
        self.board = [' ' for _ in range(9)]
        # No winner yet
        self.current_winner = None 

    # Print the current board state with X's and O's
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    # Show board positions so user knows where to play
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # List of indexes on the board that are still free
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

        # Multiline comment of expanded version of the above comprehension list
        '''
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
        '''
    
    # Check if there are any empty spaces left
    def empty_squares(self):
        return ' ' in self.board

    # Count how many empty squares are left
    def num_empty_squares(self):
        return self.board.count(' ')

    # Place a letter on the board if the square is free
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            print(f"Square {square} already taken!")
        return False

    # Check all win condions: row , column and diagonals
    def winner(self, square, letter):
        #lets check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals (only possible if square is even numbers)
        if square %2 == 0:
            diagonal1 = [self.board [i] for i in  [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board [i] for i in  [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all thse checks fail
        return False

# Main function that runs one full game of Tic Tac Toe
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # X starts the game
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # lets define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter.upper() + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line

            # If that move won the game
            if game.current_winner:
                if print_game:
                    print(f"\n🎉 {letter} Wins! 🎉")
                    print_emoji_fireworks()
                return letter # End the game with the winner
        
        # Switch player turns
        letter = 'O' if letter == 'X' else 'X'
        
    if print_game:
        print("It's a tie!") # No winner

# Game launcher and scoreboard tracker
if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0

    while True:
        # Set up players and game board
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()

        # Play a game and tet the result
        result = play(t, x_player, o_player, print_game= True)

        # Update scoreboared based on result
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

        # Show scoreboard
        print(f"\n🏆 Scoreboard:")
        print(f"X (You): {x_wins}")
        print(f"O (Computer): {o_wins}")
        print(f"Ties: {ties}\n")

        # Ask to play again
        play_again = input("Play again? y/n: ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break