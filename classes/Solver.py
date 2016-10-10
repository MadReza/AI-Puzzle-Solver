from collections import deque
from Heuristic import *
from Puzzle import Puzzle
from Queue import PriorityQueue
import time

class Solver:
    algorithm=""
    initial_puzzle = None

    def __init__(self, puzzle, algorithm="a*", heuristic="min"):
        self.algorithm = self.get_algorithm(algorithm)
        self.initial_puzzle = puzzle
        self.h = get_heuristic_function(heuristic)
        self.h_name = get_heuristic_name(heuristic)

    def get_algorithm(self, name):
        if name.lower() == "a*":
            self.a_name = "A*"
            return self.a_star
        if name.lower() == "best":
            self.a_name = "Best First"
            return self.best_first
        if name.lower() == "bfs":
            self.a_name = "Breadth first search"
            return self.bfs
        if name.lower() == "dfs":
            self.a_name = "depth first search"
            return self.dfs
        return None

    def solve(self):
        print "_________________________"
        print "Puzzle: "
        print self.initial_puzzle
        print "Algorithm: " + self.a_name
        print "Heurisitic if used: " + self.h_name

        t = time.clock()
        solution = self.algorithm()
        completed_in = time.clock() - t

        print "Time: " + `completed_in` + " seconds"

        """Backtracking to count solution"""
        current = Puzzle([1,2,3,4,5,6,7,8,0])
        start = self.initial_puzzle
        previous = solution
        steps = 0
        while current != start:
            current = previous[current]
            steps = steps + 1
        
        print "Steps: " + `steps`
        print "_________________________"
        return solution

        
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
        seen = set()    #We can use the previous_puzzle alone, However performance seems to suffer
        cost_so_far = {}
        
        puzzles_available.put(self.initial_puzzle, 0)
        previous_puzzle[self.initial_puzzle] = None
        cost_so_far[self.initial_puzzle] = 0
        
        while not puzzles_available.empty():
            current_puzzle = puzzles_available.get()
            seen.add(current_puzzle)

            if current_puzzle.solved():
                return previous_puzzle

            for new_hole_position in current_puzzle.possible_moves():
                new_board = current_puzzle.move(new_hole_position)
                new_cost = cost_so_far[current_puzzle]
                new_cost += 1      #As all directions is 1, see general comment
                if new_board not in seen or new_cost < cost_so_far[new_board]:
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
                return previous_puzzle

            for new_hole_position in current_puzzle.possible_moves():
                new_board = current_puzzle.move(new_hole_position)
                if new_board not in seen:
                    puzzles_available.append(new_board)
                    previous_puzzle[new_board] = current_puzzle
            
        return None #No Solutions found
