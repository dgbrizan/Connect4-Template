import numpy as np


class Connect4Board:



    def __init__(self, empty=0, player1=1, player2=2, rows=6, cols=7):
        self.EMPTY = empty
        self.PLAYER1 = player1
        self.PLAYER2 = player2
        self.ROWS = rows
        self.COLS = cols
        self.board = np.zeros((self.ROWS, self.COLS), dtype=np.int16)
        self.PLAYERS = (self.PLAYER1, self.PLAYER2)
        self.GAME_OVER = False



    def draw(self):
        print('Connect 4 Board:')
        for i in range(self.ROWS):
            print('|', end='')
            for j in range(self.COLS):
                if self.board[i,j] == self.PLAYER1:
                    print('X|', end='')
                elif self.board[i,j] == self.PLAYER2:
                    print('O|', end='')
                else:
                    print(' |', end='')
            print('') # Newline at the end of the row
        print(' =============')



    def add(self, col, player, just_check=False):
        # Player adds a token to a column. The token falls to the bottommost row.
        row = 0

        # Exceptional conditions
        if self.GAME_OVER or self.no_valid_moves():
            return -1
        if player not in self.PLAYERS:
            raise Exception('Illegal player: ' + str(player))
        if self.board[row, col] != 0:
            raise Exception('Illegal move attempted in col ' + str(col))

        # Okay... onto the real thing
        self.board[row, col] = player
        while row+1 < self.ROWS and self.board[row+1, col] == 0:
            self.board[row, col] = 0
            self.board[row+1, col] = player
            row += 1

        if not just_check and self.check_winner() is not None:
            print('=====>  Winner: player', player, ' <=====')

        return row



    def is_valid(self, col):
        return self.board[0, col] == self.EMPTY



    def check_winner(self, just_check=False):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row,col] == self.EMPTY:
                    continue
                # Check horizontal
                if col+3 < self.COLS and all(self.board[row,col+i] == self.board[row,col] for i in range(4)):
                    if not just_check:
                        self.GAME_OVER = True
                    return self.board[row,col]
                if row+3 < self.ROWS and all(self.board[row+i,col] == self.board[row,col] for i in range(4)):
                    if not just_check:
                        self.GAME_OVER = True
                    return self.board[row,col]
                if row+3 < self.ROWS and col+3 < self.COLS and all(self.board[row+i,col+i] == self.board[row,col] for i in range(4)):
                    if not just_check:
                        self.GAME_OVER = True
                    return self.board[row,col]
                if row-3 >= 0 and col+3 < self.COLS and all(self.board[row-i,col+i] == self.board[row,col] for i in range(4)):
                    if not just_check:
                        self.GAME_OVER = True
                    return self.board[row,col]
        return None
        


    def no_valid_moves(self):
        for i in range(self.COLS):
            if self.is_valid(i):
                return False
        return True
