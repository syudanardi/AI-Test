from Game import Game
from Problem import Problem
class Parta:

    def __init__(self):
        game = Game()
        game.main()
        problem = Problem(game.white)

if __name__ == "__main__":
    play = Parta()