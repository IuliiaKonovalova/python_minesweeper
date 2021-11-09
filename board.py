import random

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        # Create a board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bomb_planted = 0
        # Add bombs to the board
        while bomb_planted < self.num_bombs:
            # Get a random location for a bomb
            location = random.randit(0, self.dim_size**2 - 1)
            # Find the row and the column of the location
            row = location // self.dim_size
            column = location % self.dim_size
            # Check whether the space is still empty,
            # if it is not, do nothing
            # if it is empty, place the bomb and increase number of bombs
            if board[row][column] == '*':
                continue
            board[row][column] = '*'
            bomb_planted +=1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, column):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size -1, row + 1) + 1):
            for c in range(max(0, row-1), min(self.dim_size -1, row + 1) + 1):
                # Check whether the place is original 
                if r == row and c == column:
                    continue
                # Otherwise, increase the num of bombs
                if self.board[r][c] == '*':
                    num_neighboring_bombs +=1
        return num_neighboring_bombs
