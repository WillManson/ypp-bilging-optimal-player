class SequenceOfMoves:
    def __init__(self, moves, points):
        self.moves = moves
        self.points = points

    def prependMove(self, move):
        self.moves = [ move ] + self.moves
