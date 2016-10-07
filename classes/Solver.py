from Puzzle import Puzzle
from collections import deque

class Solver:
    algorithm=""
    initial_puzzle = None

    def __init__(self, puzzle, algorithm="a*"):
        self.algorithm = algorithm
        self.initial_puzzle = puzzle

    def solve(self):
        print self.initial_puzzle
        print self.algorithm

    def dfs(self):
        q = deque()
        solution_path = deque()
        q.append(self.initial_puzzle)
        seen = set()

        while len(q):
            current_puzzle = q.pop()    #FILO
            seen.add(current_puzzle)
            print current_puzzle
            print "-------"
            if current_puzzle.solved():
                print "Solved" #delete later
                return "solution" #replace by path to solution

            for new_hole_position in current_puzzle.possible_moves():
                new_board = current_puzzle.move(new_hole_position)
                if new_board not in seen:
                    q.append(new_board)
                    
                
                    
            
        return None #No Solutions found
