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
    solver = Solver(puzzle, args.algorithm)
    solver.solve()

    h = get_heuristic_function("min")
    print h(puzzle)
    print "______"
    h = get_heuristic_function("manhattan")
    print h(puzzle)
    print "______"
    h = get_heuristic_function("misplaced")
    print h(puzzle)
    print "______"


    dfs_solution = solver.dfs()
    bfs_solution = solver.bfs()
    best_first_solution = solver.best_first()
    a_star_solution = solver.a_star()
    
    solved_puzzle = Puzzle([1,2,3,4,5,6,7,8,0])
    initial_puzzle = puzzle
    #path_show(initial_puzzle, solved_puzzle, a_star_solution)



