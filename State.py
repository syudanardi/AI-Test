from Game import Game
from Player import Player
from Piece import Piece

class State:
    def __init__(self, board, white, black):
        self.board = board
        self.white = white
        self.black = black