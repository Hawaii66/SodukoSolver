from datetime import date, datetime


class BoardPrint():
    def BoardLine(self):
        return " --- "

    def FullLine(self):
        return "|" + ((self.BoardLine() * 3 + "|") * 3)

    def StraightLine(self):
        return "|"

    def BoardSpace(self):
        return "     "

    def BoardSpaceNumber(self, n):
        return "  " + str(n) + "  "

    def EmptyBoardLine(self, ):
        return self.StraightLine() + (self.BoardSpace() * 3 + self.StraightLine()) * 3

    def BoardLineNumber(self, xLine, spacing):
        currentSpace = spacing
        output = ""
        output += self.StraightLine()
        for i in range(len(xLine)):
            output += self.BoardSpaceNumber(xLine[i])
            if i == currentSpace - 1:
                output += self.StraightLine()
                currentSpace += spacing
        return output

    def FullBoard(self, board, spacing):
        currentSpacing = spacing
        output = self.FullLine()
        for i in range(len(board)):
            output += "\n"
            output += self.BoardLineNumber(board[i], spacing)
            if i == currentSpacing - 1:
                output += "\n"
                output += self.FullLine()
                currentSpacing += spacing
        return output


class Board ():
    fixedBoard = []
    board = []
    currentX = 0
    currentY = 0

    def __init__(self, _board, _board2) -> None:

        if len(_board) != 9 or len(_board[0]) != 9:
            print("Board is not of correct length")
            return
        self.board = _board
        self.fixedBoard = _board2

    def GetBoard2D(self):
        return self.board

    def PrintBoard(self):
        tempBoard = []
        for y in range(len(self.board)):
            row = []
            for x in range(len(self.board[y])):
                row.append(self.board[y][x])
            tempBoard.append(row)
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                tempBoard[y][x] = self.board[y][x] if self.board[y][x] != 0 else " "

        return BoardPrint().FullBoard(self.board, 3)

    def SolveStart(self):
        i = 0
        if self.board[self.currentY][self.currentX] != 0:
            self.MoveForward()
        self.increaseCurrent(self.currentX, self.currentY)
        before = datetime.now()
        print(before)
        while i < 10000000:
            # print(self.PrintBoard())
            success = self.Solve()
            if success == False:
                # print(self.currentX)
                # print(self.currentY)
                if self.board[self.currentY][self.currentX] == 9:
                    while self.board[self.currentY][self.currentX] == 9:
                        self.SetToZero(self.currentX, self.currentY)
                        self.SetXYtoPrev()
                    self.increaseCurrent(self.currentX, self.currentY)
                    # print(self.PrintBoard())

                else:
                    self.increaseCurrent(self.currentX, self.currentY)
                    # print(self.PrintBoard())
            else:
                # print(self.PrintBoard())
                #print("SUCCES DONE FIND CORRECT")
                # elif self.boardHasZero():
                #print("Board Has 0")
                self.MoveForward()
                self.increaseCurrent(self.currentX, self.currentY)
                # print(self.currentX)
                # print(self.currentY)
                # break

            if not self.boardHasZero():
                if self.Solve() == True:
                    print("SUCCESS")
                    print(self.PrintBoard())
                    now = datetime.now()
                    print(now)
                    print(now - before)
                    return
            i += 1
        print(i)
        print("I ran out")
        print(self.PrintBoard())

    def Solve(self):
        # All rows --
        hasZero = False
        for y in range(len(self.board)):
            contains = []
            for x in range(len(self.board)):
                current = self.board[y][x]
                for i in range(len(contains)):
                    if contains[i] == current:
                        return False
                if current != 0:
                    contains.append(current)
                else:
                    hasZero = True
        for x in range(len(self.board)):
            contains = []
            for y in range(len(self.board)):
                current = self.board[y][x]
                for i in range(len(contains)):
                    if contains[i] == current:
                        return False
                if current != 0:
                    contains.append(current)
                else:
                    hasZero = True

        for y in range(3):
            for x in range(3):
                current = []
                current.append(self.board[y * 3][x * 3])
                current.append(self.board[y * 3][x * 3 + 1])
                current.append(self.board[y * 3][x * 3 + 2])
                current.append(self.board[y * 3 + 1][x * 3])
                current.append(self.board[y * 3 + 1][x * 3 + 1])
                current.append(self.board[y * 3 + 1][x * 3 + 2])
                current.append(self.board[y * 3 + 2][x * 3])
                current.append(self.board[y * 3 + 2][x * 3 + 1])
                current.append(self.board[y * 3 + 2][x * 3 + 2])
                contains = []
                for i in range(len(current)):
                    for j in range(len(contains)):
                        if contains[j] == current[i]:
                            return False
                    if current[i] != 0:
                        contains.append(current[i])
                    else:
                        hasZero = True
        # if hasZero:
        #    return False
        return True

    def increaseCurrent(self, x, y):
        self.board[y][x] += 1

    def SetToZero(self, x, y):
        self.board[y][x] = 0

    def SetXYtoPrev(self):
        board1D = []
        board1DFixed = []
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                board1D.append(self.board[y][x])
                board1DFixed.append(self.fixedBoard[y][x])
        current = self.currentY * 9 + self.currentX
        while True:
            current -= 1
            if current == -1:
                print(self.PrintBoard())
                print("ERROR, SODUKO WRONG OR BAD CODE")
                return
            if board1DFixed[current] == 0:
                break

        tempX = current
        while tempX >= 9:
            tempX -= 9
        self.currentX = tempX
        self.currentY = round((current - self.currentX) / 9)

        # while True:
        #    if current < 9:
        #        self.currentX = current
        #        return
        #    current -= 9
        #    self.currentY -= 1

    def MoveForward(self):
        board1D = []
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                board1D.append(self.board[y][x])

        current = self.currentY * 9 + self.currentX
        while True:
            if board1D[current] == 0:
                break
            else:
                self.currentX += 1
                if self.currentX == 9:
                    self.currentX = 0
                    self.currentY += 1

            current += 1

    def boardHasZero(self):
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                if self.board[y][x] == 0:
                    return True
        return False


board = Board([
    [5, 0, 8, 0, 0, 0, 0, 0, 0],
    [1, 0, 7, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 2],
    [0, 0, 0, 0, 3, 1, 4, 7, 0],
    [0, 0, 0, 0, 6, 7, 0, 3, 0],
    [4, 0, 3, 0, 5, 0, 0, 0, 0],
    [0, 0, 1, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 5]
], [
    [5, 0, 8, 0, 0, 0, 0, 0, 0],
    [1, 0, 7, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 2],
    [0, 0, 0, 0, 3, 1, 4, 7, 0],
    [0, 0, 0, 0, 6, 7, 0, 3, 0],
    [4, 0, 3, 0, 5, 0, 0, 0, 0],
    [0, 0, 1, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 5]
])

print(board.SolveStart())

# print(board.PrintBoard())
# board.increaseNext()
# board.increaseNext()
# board.increaseNext()
# board.increaseNext()
# board.increaseNext()
#board.DecreasePrev(0, 0)
# print(board.PrintBoard())
