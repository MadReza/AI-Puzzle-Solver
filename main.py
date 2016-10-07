from classes.Helper import getCmdArgs
from classes.Puzzle import Puzzle

if __name__ == '__main__':
    args = getCmdArgs()
    print args.algorithm
    print type(args.thePuzzle[0])
    puzzle = Puzzle(args.thePuzzle)
    print puzzle
