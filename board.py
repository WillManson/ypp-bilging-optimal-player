import random
execfile("brute_forcer.py")
execfile("sequence_of_moves.py")
execfile("board_scanner.py")

class Board:
    def __init__(self):
        self.pieces = [[0 for column in range(6)] for row in range(12)]
        self.points = 0

    def setBoard(self, pieces):
        self.pieces = pieces

    def printBoard(self):
        for row in self.pieces:
            for column in row:
                print column,
            print "\n",

    def fillBoard(self):
        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[i])):
                if self.pieces[i][j] == 0:
                    self.fillSpace(i, j)

    def fillSpace(self, i, j):
        while self.pieces[i][j] == 0:
            for k in range(i, len(self.pieces) - 1):
                self.pieces[k][j] = self.pieces[k + 1][j]
            self.pieces[len(self.pieces) - 1][j] = random.randint(1, 5)

    def searchForMatchesAndClear(self):
        self.points = 0
        matches = []
        currentTileType = 0
        currentTileMatchCount = 0
        sizeOfCombo = 0

        for j in range(len(self.pieces[0])):
            for i in range(len(self.pieces)):
                if currentTileType == self.pieces[i][j]:
                    currentTileMatchCount += 1
                else:
                    currentTileType = self.pieces[i][j]
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

        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[i])):
                if currentTileType == self.pieces[i][j]:
                    currentTileMatchCount += 1
                else:
                    currentTileType = self.pieces[i][j]
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
            self.pieces[match[0]][match[1]] = 0

    def scorePointsAndReplenishBoard(self):
        while True:
            self.searchForMatchesAndClear()
            self.fillBoard()
            if (self.points == 0):
                break
            print "Score ",self.points

    def swapPieces(self, i, j):
        temp = self.pieces[i][j]
        self.pieces[i][j] = self.pieces[i][j + 1]
        self.pieces[i][j + 1] = temp

    def performSwap(self, i, j):
        self.swapPieces(i, j)
        self.scorePointsAndReplenishBoard()

    def getCopy(self):
        copy = Board()
        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[i])):
                copy.pieces[i][j] = self.pieces[i][j]
        return copy

bs = BoardScanner()

while (True):
    bs.updateBoard()
    pieces = bs.getBoard()
    b = Board()
    b.setBoard(pieces)
    brute = BruteForcer()
    optimal = brute.getOptimalSequenceOfMoves(b, 2)
    print optimal.moves
    print optimal.points
    bs.makeMoves(optimal.moves)
    raw_input("Press enter when you are ready")
