# lists of lists
board = [['_']*3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

weird_board = [['_']*3]*3 # list element is list, reference type
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

# list sort
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(fruits)
fruits.sort()
print(fruits)