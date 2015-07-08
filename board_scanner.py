import PIL.Image
import PIL.ImageStat
import pyscreenshot
import time
from pymouse import PyMouse

class BoardScanner:
    def __init__(self):
        self.pixelGap = 45
        self.mouse = PyMouse()
        position = self.mouse.position()
        self.intPosition = (int(round(position[0])), int(round(position[1])))
        self.pieceMap = {}
        self.numberOfDistinctPieces = 0
        self.boardPieces = [[0 for column in range(6)] for row in range(12)]
        self.simplifiedBoard = [[0 for column in range(6)] for row in range(12)]

    def getBoard(self):
        return self.simplifiedBoard

    def updateBoard(self):
        self.boardPieces = [[0 for column in range(6)] for row in range(12)]
        self.simplifiedBoard = [[0 for column in range(6)] for row in range(12)]
        self.readBoardFromScreen()
        self.reduceBoard()

    def readBoardFromScreen(self):
        image = pyscreenshot.grab()
        pixelColours = image.load()

        for row in range(12):  
            for column in range(6):
                pieceXPosition = self.intPosition[0] + (column * self.pixelGap)
                pieceYPosition = self.intPosition[1] + (row * self.pixelGap)
                # Do not multiply for non-retina displays
                # pixel = pixelColours[pieceXPosition, pieceYPosition]
                # Multiply by 2 to correct for retina displays 
                pixel = pixelColours[pieceXPosition * 2, pieceYPosition * 2]
                self.boardPieces[row][column] = (256 * 256 * pixel[0]) + (256 * pixel[1]) + pixel[2]

    def reduceBoard(self):
        for row in range(12):  
            for column in range(6):
                self.resolvePiece(row, column)

    def resolvePiece(self, row, column):
        pieceColour = self.boardPieces[row][column]            
        if pieceColour in self.pieceMap:
            self.simplifiedBoard[row][column] = self.pieceMap[pieceColour]
        else:
            if row < 3:
                # Water cannot rise above the third-from-top piece
                # so any new colour detected there MUST be due to
                # a new piece
                self.recordNewPiece(pieceColour)
                self.simplifiedBoard[row][column] = self.numberOfDistinctPieces
            else:
                # The new colour may be due to the given piece being
                # underwater
                self.askUserToIdentifyNewPiece(row, column)

    def recordNewPiece(self, pieceColour):
        self.numberOfDistinctPieces += 1
        print "We now have",
        print self.numberOfDistinctPieces
        self.pieceMap[pieceColour] = self.numberOfDistinctPieces

    def askUserToIdentifyNewPiece(self, row, column):
        pieceColour = self.boardPieces[row][column]
        self.outputPiecesWithXInGivenPosition(row, column)
        print "Please identify the piece marked X"
        print "Enter the piece number according to the output above"
        print "or enter " + `(self.numberOfDistinctPieces + 1)` + " if the piece is new (i.e. it doesn't appear "  
        print "in the output above:",
        userInput = input("")
        if userInput > 0 and userInput <= self.numberOfDistinctPieces:
            self.pieceMap[pieceColour] = userInput
            self.simplifiedBoard[row][column] = userInput
        else:
            self.recordNewPiece(pieceColour)
            self.simplifiedBoard[row][column] = self.numberOfDistinctPieces

    def outputPiecesWithXInGivenPosition(self, xRow, xColumn):
        for row in range(12):  
            for column in range(6):
                if xRow == row and xColumn == column:
                    print "X",
                else:
                    print self.simplifiedBoard[row][column],
            print            

    def makeMoves(self, moves):
        for move in moves:
            self.makeMove(move)
            time.sleep(1)

    def makeMove(self, move):
        row = move[0]
        column = move[1]
        xPixel = self.intPosition[0] + (column * self.pixelGap)
        yPixel = self.intPosition[1] + (row * self.pixelGap)
        self.mouseClick(xPixel, yPixel)

    def mouseClick(self, x, y):
        self.mouse.click(x, y, 1)
