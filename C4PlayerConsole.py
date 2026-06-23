import random

class C4PlayerConsole:

    def __init__(self, player_num):
        self.player_num = player_num

    def move(self, board):
        valid_entry = False
        while not valid_entry:
            try:
                col = int(input('Drop into col: '))
            except:
                print('Number of col between 0 and 6')
            if board.add(col, self.player_num) >= 0:
                valid_entry = True

