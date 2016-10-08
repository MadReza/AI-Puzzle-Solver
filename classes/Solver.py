from Puzzle import Puzzle
from collections import deque
from Queue import PriorityQueue
from Heuristic import manhattan_distance

class Solver:
    algorithm=""
    initial_puzzle = None

    def __init__(self, puzzle, algorithm="a*"):
        self.algorithm = algorithm
        self.initial_puzzle = puzzle

    def solve(self):
        print self.initial_puzzle
        print self.algorithm

    def best_first(self):
        puzzles_available = PriorityQueue()
        previous_puzzle = {}
        seen = set()    #We can use the previous_puzzle alone, However performance lowers
        
        puzzles_available.put(self.initial_puzzle, 0)
        previous_puzzle[self.initial_puzzle] = None
        
        while not puzzles_available.empty():
            current_puzzle = puzzles_available.get()
            seen.add(current_puzzle)

            if current_puzzle.solved():
                print "Solved" #delete later
                return previous_puzzle

            for new_hole_position in current_puzzle.possible_moves():
                new_board = current_puzzle.move(new_hole_position)
                if new_board not in seen:
                    priority = manhattan_distance(new_board)
                    puzzles_available.put(new_board, priority)
                    previous_puzzle[new_board] = current_puzzle
        
        return None #No Solutions found

    """
        TODO: Clean up BFS and DFS.
              Same crap
    """
    def bfs(self):
        puzzles_available = deque()
        previous_puzzle = {}
        seen = set()    #We can use the previous_puzzle alone, However performance lowers

        puzzles_available.append(self.initial_puzzle)
        previous_puzzle[self.initial_puzzle] = None

        while len(puzzles_available):
            current_puzzle = puzzles_available.popleft()    #FIFO
            seen.add(current_puzzle)

            if current_puzzle.solved():
                print "Solved" #delete later
                return previous_puzzle

            for new_hole_position in current_puzzle.possible_moves():
                new_board = current_puzzle.move(new_hole_position)
                if new_board not in seen:
                    puzzles_available.append(new_board)
                    previous_puzzle[new_board] = current_puzzle
        return None #No Solutions found

    def dfs(self):
        puzzles_available = deque()
        previous_puzzle = {}    
        seen = set()    #We can use the previous_puzzle alone, However performance lowers
        
        puzzles_available.append(self.initial_puzzle)
        previous_puzzle[self.initial_puzzle] = None

        while len(puzzles_available):
            current_puzzle = puzzles_available.pop()    #FILO
            seen.add(current_puzzle)
            
            if current_puzzle.solved():
                print "Solved" #delete later
                return previous_puzzle

            for new_hole_position in current_puzzle.possible_moves():
                new_board = current_puzzle.move(new_hole_position)
                if new_board not in seen:
                    puzzles_available.append(new_board)
                    previous_puzzle[new_board] = current_puzzle
            
        return None #No Solutions found
