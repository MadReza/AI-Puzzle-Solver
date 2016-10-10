from classes.Helper import getCmdArgs
from classes.Puzzle import Puzzle
from classes.Solver import Solver
from classes.Heuristic import *


def path_show(start, end, path):
    current = end
    previous = path      #As this is a dictionary with previous caller
    path = [current]

    while current != start:
        current = previous[current]
        path.append(current)

    path.reverse()

    for x in path:
        print x
        print "---------"



if __name__ == '__main__':
    args = getCmdArgs()
    puzzle = Puzzle(args.thePuzzle)
    
    solver = Solver(puzzle, args.algorithm, args.heuristic)
    solution = solver.solve()
    
    solved_puzzle = Puzzle([1,2,3,4,5,6,7,8,0])
    initial_puzzle = puzzle
    if args.verbose:
        path_show(initial_puzzle, solved_puzzle, solution)

    print "______TEST______"
    ##########A*##################
    a = "a*"
    h = "manhattan"
    s = Solver(puzzle, a, h).solve()
    a = "a*"
    h = "misplaced"
    s = Solver(puzzle, a, h).solve()
    a = "a*"
    h = "min"
    s = Solver(puzzle, a, h).solve()
    a = "a*"
    h = "linear"
    s = Solver(puzzle, a, h).solve()
    a = "a*"
    h = "nilsson"
    s = Solver(puzzle, a, h).solve()
    ########Best_FIRST#############
    a = "best"
    h = "manhattan"
    s = Solver(puzzle, a, h).solve()
    a = "best"
    h = "misplaced"
    s = Solver(puzzle, a, h).solve()
    a = "best"
    h = "min"
    s = Solver(puzzle, a, h).solve()
    a = "best"
    h = "linear"
    s = Solver(puzzle, a, h).solve()
    a = "best"
    h = "nilsson"
    s = Solver(puzzle, a, h).solve()
    ###############BFS#############
    a = "bfs"
    h = "manhattan"
    s = Solver(puzzle, a, h).solve()
    a = "bfs"
    h = "misplaced"
    s = Solver(puzzle, a, h).solve()
    a = "bfs"
    h = "min"
    s = Solver(puzzle, a, h).solve()
    a = "bfs"
    h = "linear"
    s = Solver(puzzle, a, h).solve()
    a = "bfs"
    h = "nilsson"
    s = Solver(puzzle, a, h).solve()
    ###############BFS#############
    a = "dfs"
    h = "manhattan"
    s = Solver(puzzle, a, h).solve()
    a = "dfs"
    h = "misplaced"
    s = Solver(puzzle, a, h).solve()
    a = "dfs"
    h = "min"
    s = Solver(puzzle, a, h).solve()
    a = "dfs"
    h = "linear"
    s = Solver(puzzle, a, h).solve()
    a = "dfs"
    h = "nilsson"
    s = Solver(puzzle, a, h).solve()     
    #manual testing#    
    """
    dfs_solution = solver.dfs()
    bfs_solution = solver.bfs()
    best_first_solution = solver.best_first()
    a_star_solution = solver.a_star()
    """
    
    



