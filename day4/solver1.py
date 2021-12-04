import sys
f = open(sys.argv[1], "r")

class Board:
    def __init__(self, boardArray, coveredNumbers, numbers):
        self.board = boardArray
        self.coveredNumbers = coveredNumbers
        self.numbers = numbers
        self.makeWinningsSet()

    def makeWinningsSet(self):
        self.currentStatus = []
        self.currentStatus += [[self.board[i][i] for i in range(5)]] #neg diagonal
        self.currentStatus += [[self.board[4 - i][i] for i in range(5)]] #pos diagonal
        for j in range(5): #rows
            self.currentStatus += [[self.board[i][j] for i in range(5)]]
        for j in range(5): #columns
            self.currentStatus += [[self.board[j][i] for i in range(5)]]

    def isBoardWon(self):
        for line in self.currentStatus:
            if len(line) == 0:
                return True
        return False

    def toString(self):
        print("Board")
        print(self.board)
        print("CoveredNumbers")
        print(self.coveredNumbers)
        print("Status")
        print(self.currentStatus)

def createBoard(lines, index):
        index += 1
        board = []
        numbers = set()
        for i in range(5):
            line = [int(x) for x in lines[index + i].split()]
            numbers.update(line)
            board += [line]
        return Board(board, set(), numbers), index + 5

numbersInput = f.readline().strip()
numbersInput = [int(x) for x in numbersInput.split(",")]
boards = []
lines = f.readlines()
index = 0

while index < len(lines):
    board, index = createBoard(lines, index)
    boards += [board]


for board in boards:
    board.toString()