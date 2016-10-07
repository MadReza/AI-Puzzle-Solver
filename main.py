from classes.Helper import getCmdArgs
from classes.Puzzle import Puzzle
from classes.Solver import Solver

if __name__ == '__main__':
    args = getCmdArgs()
    puzzle = Puzzle(args.thePuzzle)
    solver = Solver(puzzle, args.algorithm)


