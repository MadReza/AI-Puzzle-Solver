from collections import deque
from Heuristic import *
from Puzzle import Puzzle
from Queue import PriorityQueue

class Solver:
    algorithm=""
    initial_puzzle = None

    def __init__(self, puzzle, algorithm="a*", heuristic="min"):
        self.algorithm = algorithm
        self.initial_puzzle = puzzle
        self.h = get_heuristic_function(heuristic)

    def solve(self):
        print self.initial_puzzle
        print self.algorithm

    """
        A* and Dijkstra's require a value for the each location.
        This is hard to set as every location is the same.

        However, looking at the percpective of the fields being changed by the movement
        We can probably add values to each location.
            e.g.: Movement to x,y causes 3 locations to lose heuristic value(manhanttan for example).
    """
    def a_star(self):
        puzzles_available = PriorityQueue()
        previous_puzzle = {}
        seen = set()    #We can use the previous_puzzle alone, However performance lowers
        cost_so_far = {}
        
        puzzles_available.put(self.initial_puzzle, 0)
        previous_puzzle[self.initial_puzzle] = None
        cost_so_far[self.initial_puzzle] = 0
        
        while not puzzles_available.empty():
            current_puzzle = puzzles_available.get()
            seen.add(current_puzzle)

            if current_puzzle.solved():
                print "Solved" #delete later
                return previous_puzzle

            for new_hole_position in current_puzzle.possible_moves():
                new_board = current_puzzle.move(new_hole_position)
                new_cost = cost_so_far[current_puzzle]
                new_cost += 1      #As all directions is 1, see general comment
                if new_board not in seen:
                    priority = self.h(new_board) + new_cost
                    puzzles_available.put(new_board, priority)
                    previous_puzzle[new_board] = current_puzzle
                    cost_so_far[new_board] = new_cost
        
        return None #No Solutions found

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
                    priority = self.h(new_board)
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
