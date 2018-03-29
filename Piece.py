class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.dead = False

    # retrieves coordinate of the piece
    def getCoordinate(self):
        return (self.x, self.y)

    def setRow(self, y):
        self.y = y

    def setCol(self, x):
        self.x = x

    def remove(self):
        self.dead = True