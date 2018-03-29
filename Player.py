class Player:
    MAX_PIECES = 12

    def __init__(self, color):
        self.color = color
        self.pieces = []

    # adds a piece into the player's list of pieces
    def addPiece(self, piece):
        self.pieces.append(piece)

    # gets the list of pieces
    def getPieces(self):
        return self.pieces

    def removePiece(self, piece):
        self.pieces.remove(piece)