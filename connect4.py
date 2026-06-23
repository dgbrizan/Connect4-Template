from Connect4Board import Connect4Board
from C4PlayerConsole import C4PlayerConsole

board = Connect4Board()
p1 = C4PlayerConsole(1)
p2 = C4PlayerConsole(2)

board.draw()
while not board.GAME_OVER:
    p1.move(board)
    board.draw()
    if not board.GAME_OVER:
        p2.move(board)
        board.draw()

