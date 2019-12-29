board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'O'
print(weird_board)