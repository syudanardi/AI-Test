from Player import Player
from Piece import Piece
import sys

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

    def checkUp(self, coordinate, state):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the top edge of the board
        if (yCoor <= 0):
            return False

        return state.board[yCoor - 1][xCoor]

    def checkDown(self, coordinate, state):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the bottom edge of the board
        if (yCoor >= 7):
            return 0

        return state.board[yCoor + 1][xCoor]

    def checkLeft(self, coordinate, state):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the left edge of the board
        if (xCoor <= 0):
            return 0
        return state.board[yCoor][xCoor - 1]

    def checkRight(self, coordinate, state):
        xCoor = coordinate[0]
        yCoor = coordinate[1]

        # check for cases when the piece is at/near the right edge of the board
        if (xCoor >= 7):
            return 0

        return state.board[yCoor][xCoor + 1]

    def doubleCheck(self, dir, cord, state):
        col = cord[0]
        row = cord[1]
        if dir.__name__ == "checkUp":
            return dir(self,(col,row-1), state)
        elif dir.__name__ == "checkDown":
            return dir(self,(col,row+1), state)
        elif dir.__name__ == "checkLeft":
            return dir(self,(col-1,row), state)
        elif dir.__name__ == "checkRight":
            return dir(self, (col + 1, row), state)

    def movePiece(self,dir,pieceIndex,state):
        amount = 1
        if dir[0] == "2":
            amount = 2
            dir = dir[1:]

        col = state.white.getPieces()[pieceIndex].getCoordinate()[0]
        row = state.white.getPieces()[pieceIndex].getCoordinate()[1]
        state.board[row][col] = '-'
        if dir == "up":
            row -= amount
            state.white.getPieces()[pieceIndex].setRow(row)
        elif dir == "down":
            row += amount
            state.white.getPieces()[pieceIndex].setRow(row)
        elif dir == "left":
            col -= amount
            state.white.getPieces()[pieceIndex].setCol(col)
        elif dir == "right":
            col += amount
            state.white.getPieces()[pieceIndex].setCol(col)

        state.board[row][col] = 'O'
        return True

    def isDead(self,piece,state):
        x = piece.getCoordinate()[0]
        y = piece.getCoordinate()[1]
        P = None
        if piece.color == "black":
            P = "O"
        elif piece.color == "white":
            P = "@"
        if P is None:
            sys.exit("fucked up")
        if (self.checkUp((x,y),state) == P or self.checkUp((x,y),state) == "X") and (self.checkDown((x,y),state) == P or self.checkDown((x,y),state) == "X"):
            return True
        elif (self.checkLeft((x,y),state) == P or self.checkLeft((x,y),state) == "X") and (self.checkRight((x,y),state) == P or self.checkRight((x,y),state) == "X"):
            return True
        return False

    def printBoard(self):
        for i in range(self.BOARD_ROW_SIZE):
            print(self.board[i])