class BruteForcer:
    def getOptimalSequenceOfMoves(self, board, sequenceLength):
        optimalSequenceOfMoves = SequenceOfMoves([], 0)

        if (sequenceLength == 0):
            return optimalSequenceOfMoves

        for i in range(len(board.pieces)):
            for j in range(len(board.pieces[i]) - 1):
                copy = board.getCopy()
                copy.swapPieces(i, j)
                copy.searchForMatchesAndClear()                
                if (copy.points == 0):
                    newSequenceOfMoves = self.getOptimalSequenceOfMoves(copy, sequenceLength - 1)
                    newSequenceOfMoves.prependMove([i, j])
                    newSequenceOfMoves.points -= 1
                    if (newSequenceOfMoves.points > optimalSequenceOfMoves.points):
                        optimalSequenceOfMoves = newSequenceOfMoves
                else:
                    newSequenceOfMoves = SequenceOfMoves([[i, j]], copy.points - 1)
                    if (newSequenceOfMoves.points > optimalSequenceOfMoves.points):
                        optimalSequenceOfMoves = newSequenceOfMoves

        return optimalSequenceOfMoves
