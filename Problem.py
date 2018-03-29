from Piece import Piece
from Player import Player
from Game import Game

class Problem(Game):

    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        Game.__init__(self)
        self.readBoard()
        self.assignCoordinates()
        initial = self.white.getPieces()
        goal = None
        self.initial = initial
        self.goal = goal
        print(self.actions(initial))

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

        action = []
        for i in range(len(state)):
            cord = state[i].getCoordinate()
            if Game.checkUp(self, cord) == '-':
                action.append((i,"up"))
            elif Game.doubleCheck(self, Game.checkUp, cord) == '-':
                action.append((i,"dup"))
            if Game.checkLeft(self,cord) == '-':
                action.append((i,"left"))
            elif Game.doubleCheck(self, Game.checkLeft, cord) == '-':
                action.append((i,"dleft"))
            if Game.checkDown(self,cord) == '-':
                action.append((i,"down"))
            elif Game.doubleCheck(self, Game.checkDown, cord) == '-':
                action.append((i,"ddown"))
            if Game.checkRight(self,cord) == '-':
                action.append((i,"right"))
            elif Game.doubleCheck(self, Game.checkRight, cord) == '-':
                action.append((i,"dright"))
        return action
    """
    def result(self, state, action):
        ""Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state).""
        raise NotImplementedError

    def goal_test(self, state):
        ""Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough.""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        ""Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path.""
        return c + 1

    def value(self, state):
        ""For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value.""
        raise NotImplementedError
        
    """