3_1_7_1
row = []

for i in range(8):
    row.append(WHITE_PAWN)
---
row = [WHITE_PAWN for i in range(8)]
---
ex.1
quares = [x ** 2 for x in range(10)]
---
ex.2
twos = [2 ** i for i in range(8)]
---
ex.3
odds = [x for x in squares if x % 2 != 0 ]
-------
3_1_7_2
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
---
board = [[EMPTY for i in range(8)] for j in range(8)]
#the inner part creates a row, the outer part bluids a list of rows.
-------
3_1_7_3
EMPTY = "_"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board [0] [0] = ROOK
board [0] [7] = ROOK
board [7] [0] = ROOK 
board [7] [7] = ROOK 

print(board)