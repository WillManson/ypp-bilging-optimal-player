import random

class Board:
    def __init__(self):
        self.board = [[0 for column in range(6)] for row in range(12)]
        self.points = 0

    def printBoard(self):
        for row in self.board:
            for column in row:
                print column,
            print "\n",

    def fillBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    self.fillSpace(i, j)

    def fillSpace(self, i, j):
        while self.board[i][j] == 0:
            for k in range(i, len(self.board) - 1):
                self.board[k][j] = self.board[k + 1][j]
            self.board[len(self.board) - 1][j] = random.randint(1, 5)

    def searchForMatchesAndClear(self):
        self.points = 0
        matches = []
        currentTileType = 0
        currentTileMatchCount = 0
        sizeOfCombo = 0

        for j in range(len(self.board[0])):
            for i in range(len(self.board)):
                if currentTileType == self.board[i][j]:
                    currentTileMatchCount += 1
                else:
                    currentTileType = self.board[i][j]
                    currentTileMatchCount = 1

                if currentTileMatchCount == 3:
                    matches.append([i - 2, j])
                    matches.append([i - 1, j])
                    matches.append([i    , j])
                    sizeOfCombo += 1
                    self.points += 3
                if (currentTileMatchCount > 3):
                    matches.append([i, j])
                    self.points += 2
            currentTileType = 0
            currentTileMatchCount = 0

        currentTileType = 0
        currentTileMatchCount = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if currentTileType == self.board[i][j]:
                    currentTileMatchCount += 1
                else:
                    currentTileType = self.board[i][j]
                    currentTileMatchCount = 1

                if currentTileMatchCount == 3:
                    matches.append([i, j - 2])
                    matches.append([i, j - 1])
                    matches.append([i, j])
                    sizeOfCombo += 1
                    self.points += 3
                if (currentTileMatchCount > 3):
                    matches.append([i, j])
                    self.points += 2
            currentTileType = 0
            currentTileMatchCount = 0

        self.points *= sizeOfCombo

        self.clearMatches(matches)

    def clearMatches(self, matches):
        for match in matches:
            self.board[match[0]][match[1]] = 0

    def scorePointsAndReplenishBoard(self):
        while True:
            self.searchForMatchesAndClear()
            self.fillBoard()
            if (self.points == 0):
                break
            print "Score ",self.points

    def swapPieces(self, i, j):
        temp = self.board[i][j]
        self.board[i][j] = self.board[i][j + 1]
        self.board[i][j + 1] = temp

    def performSwap(self, i, j):
        swapPieces(i, j)
        self.scorePointsAndReplenishBoard()

    def getCopy(self):
        copy = Board()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                copy.board[i][j] = self.board[i][j]
        return copy

    def getPointsForSwap(self, i, j):
        copy = self.getCopy()
        copy.swapPieces(i, j)
        copy.searchForMatchesAndClear()
        return copy.points

class BruteForcer:
    def __init__(self, b):
        self.b = b

    def getOptimalMove(self):
        bestMove = [ 0, 0 ]
        bestMovePoints = 0
        for i in range(len(b.board)):
            for j in range(len(b.board[i]) - 1):
                points = b.getPointsForSwap(i, j)
                if (points > bestMovePoints):
                    bestMove = [ i, j ]
                    bestMovePoints = points
        return bestMove

b = Board()
b.fillBoard()
b.scorePointsAndReplenishBoard()
bf = BruteForcer(b)
print bf.getOptimalMove()
b.printBoard()
