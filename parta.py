from Game import Game
from Problem import Problem
import sys
from Node import Node


class Parta:

    def __init__(self):
        problem = Problem()
        #self.iterative_deepening_search(problem)



    def iterative_deepening_search(self, problem):
        """[Figure 3.18]"""
        for depth in range(sys.maxsize):
            result = self.depth_limited_search(problem, depth)
            if result != 'cutoff':
                return result

    def depth_limited_search(self, problem, limit=1):
        """[Figure 3.17]"""
        def recursive_dls(node, problem, limit):
            if problem.goal_test(node.state):
                return node
            elif limit == 0:
                return 'cutoff'
            else:
                cutoff_occurred = False
                for i in range(len(node.state.board)):
                    print(node.state.board[i])
                print('\n')
                for child in node.expand(problem):
                    result = recursive_dls(child, problem, limit - 1)
                    if result == 'cutoff':
                        cutoff_occurred = True
                    elif result is not None:
                        return result
                return 'cutoff' if cutoff_occurred else None

        # Body of depth_limited_search:
        return recursive_dls(Node(problem.initial), problem, limit)

if __name__ == "__main__":
    play = Parta()