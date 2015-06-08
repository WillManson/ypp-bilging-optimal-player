import random

class Board:
	def __init__(self):
		self.board = [[0 for column in range(6)] for row in range(12)]

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
			print "Update"
			self.printBoard()
		
b = Board()
b.fillBoard()