import PIL.Image
import PIL.ImageStat
import pyscreenshot
from pymouse import PyMouse

class BoardScanner:
    def __init__(self):
        self.pixelGap = 45
        mouse = PyMouse()
        position = mouse.position()
        self.intPosition = (int(round(position[0])), int(round(position[1])))

    def getBoardFromScreen(self):
        boardPieces = [[0 for column in range(6)] for row in range(12)]
        image = pyscreenshot.grab()
        pixelColours = image.load()

        for column in range(6):
            for row in range(12):  
                pieceXPosition = self.intPosition[0] + (column * self.pixelGap)
                pieceYPosition = self.intPosition[1] + (row * self.pixelGap)
                # Do not multiply for non-retina displays
                # pixel = pixelColours[pieceXPosition, pieceYPosition]
                # Multiply by 2 to correct for retina displays 
                pixel = pixelColours[pieceXPosition * 2, pieceYPosition * 2]
                boardPieces[row][column] = (256 * 256 * pixel[0]) + (256 * pixel[1]) + pixel[2]

        return boardPieces

bs = BoardScanner()
board = bs.getBoardFromScreen()
print board
