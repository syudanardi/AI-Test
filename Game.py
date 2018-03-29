from Player import Player
from Piece import Piece

class Game:

    BOARD_ROW_SIZE = 8
    BOARD_COL_SIZE = 8
    board = []
    white = None
    black = None
    corner = None

    def main(self):
        self.readBoard()
        self.assignCoordinates()

        # Debugging
        # self.printBoard()
        # self.printCommand()
        # self.printPieces()

        #if (self.command == "Moves"):
        #    self.moves()
        #else:
        #    self.massacre()

    def __init__(self):
        self.board = []
        self.white = Player("white")
        self.black = Player("black")
        self.corner = Player("corner")

    def readBoard(self):
        # read the board configuration per row
        for i in range(self.BOARD_ROW_SIZE):
            inputs = input()
            self.board.append([x for x in inputs if x !=' '])

        # read the command (Moves/Massacre)
        self.command = input()

    def assignCoordinates(self):
        for row in range(self.BOARD_ROW_SIZE):
            for col in range(self.BOARD_COL_SIZE):
                if self.board[row][col] == 'X':
                    self.corner.addPiece(Piece("corner", col, row))
                elif self.board[row][col] == 'O':
                    self.white.addPiece(Piece("white", col, row))
                elif self.board[row][col] == '@':
                    self.black.addPiece(Piece("black", col, row))
        print([x.getCoordinate() for x in self.corner.getPieces()])
        print([x.getCoordinate() for x in self.white.getPieces()])
        print([x.getCoordinate() for x in self.black.getPieces()])

    """
    def checkUp(self, coordinate):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the top edge of the board
        if (yCoor == 0):
            return False

        return self.board[yCoor - 1][xCoor]

    def checkDown(self, coordinate):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the bottom edge of the board
        if (yCoor == 7):
            return 0

        return self.board[yCoor + 1][xCoor]

    def checkLeft(self, coordinate):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the left edge of the board
        if (xCoor == 0):
            return 0

        return self.board[yCoor][xCoor - 1]

    def checkRight(self, coordinate):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the right edge of the board
        if (xCoor == 7):
            return 0

        return self.board[yCoor][xCoor + 1]
    """