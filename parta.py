from Problem import Problem

class Game:

    BOARD_ROW_SIZE = 8
    BOARD_COL_SIZE = 8
    board = []
    white = None
    black = None

    def readBoard(self):
        # read the board configuration per row
        for i in range(self.BOARD_ROW_SIZE):
            inputs = input()
            self.board.append([x for x in inputs if x !=' '])

        # read the command (Moves/Massacre)
        self.command = input()

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


if __name__ == "__main__":
    game = Game()
    game.main()