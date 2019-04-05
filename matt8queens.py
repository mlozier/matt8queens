# Matt Lozier's 8 Queens Solution in Python.
#
# Thanks to Eilon Lipton (elipton@microsoft.com) for his logic
# in implementing the addQueen() function, which I adapted to Python
# from his C implementation.

# This 2D array (err in Python lists of lists) is one solution

board = [[0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0]]

def clearBoard(board):
    for i in range(8):
        for j in range(8):
            board[i][j] = 0

def printBoard(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                print("Q", end="")
            else:
                print("X", end="")
        print("")
    print("")

def checkColsOK(board):
    for i in range(8):
        sum = 0
        for j in range(8):
            sum += board[j][i]
        if sum > 1:
            return 0




def checkRowsOK(board):
    for i in range(8):
        sum = 0
        for j in range (8):
            sum += board[i][j]
        if sum > 1:
            return 0


def checkDiagsOK(board):

# left to right, bottom up
    counter = 8
    sum = 0

    for i in range(8):
        x = i
        y = 0
        for j in range(counter):
            #print(board[y][x], end="")
            sum += board[y][x]
            x += 1
            y +=1
        counter -= 1

        #print("")
        #print("There are ", end="")
        #print(sum, end="")
        #print(" queens in this diagonal.")
        if sum > 1:
            return 0
        sum = 0


# right to left, top down
    counter = 8
    sum = 0

    for i in range(8):
        x = i
        y = 0
        for j in range(counter):
            #print(board[x][y], end="")
            sum += board[x][y]
            x += 1
            y +=1
        counter -= 1

        #print("")
        #print("There are ", end="")
        #print(sum, end="")
        #print(" queens in this diagonal.")

        if sum > 1:
            return 0
        sum = 0


# right to left, bottom up
    counter = 8
    sum = 0

    for i in reversed(range(8)):
        x = i
        y = 0
        for j in range(counter):
            #print(board[x][y], end="")
            sum += board[x][y]
            x -= 1
            y += 1
        counter -= 1

        #print("")
        #print("There are ", end="")
        #print(sum, end="")
        #print(" queens in this diagonal.")

        if sum > 1:
            return 0
        sum = 0

# left to right, top down
    counter = 8
    sum = 0

    for i in range(8):
        x = 7
        y = i
        for j in range(counter):
            #print(board[x][y], end="")
            sum += board[x][y]
            x -= 1
            y += 1
        counter -= 1

        #print("")
        #print("There are ", end="")
        #print(sum, end="")
        #print(" queens in this diagonal.")

        if sum > 1:
            return 0
        sum = 0

def addQueen(board, col):

    row = 0

    for row in range(8):
        board[row][col] = 1
        if (checkRowsOK(board) != 0 and checkDiagsOK(board) != 0):
            if col == 7:
                printBoard(board)
            else:
                addQueen(board, col + 1)
        board[row][col] = 0


clearBoard(board)
addQueen(board, 0)

#if checkDiagsOK(board) != 0:
#    print("Diagonals are OK!")

#if checkRowsOK(board) != 0:
#    print("Rows are OK!")

#if checkRowsOK(board) != 0:
#    print ("Cols are OK!")

#printBoard(board)

#clearBoard(board)

#printBoard(board)