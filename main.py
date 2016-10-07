from classes.Helper import getCmdArgs
from classes.Puzzle import Puzzle

if __name__ == '__main__':
    args = getCmdArgs()
    print args.algorithm
    print type(args.thePuzzle[0])
    puzzle = Puzzle(args.thePuzzle)
    print puzzle.possible_moves()
    print hash(puzzle)
    print "---------"
    x = puzzle.move(1)
    print x
    print hash(x)
    print "---------"
    x = puzzle.move(3)
    print x
    print hash(x)
    print "---------"
    x = puzzle.move(5)
    print x
    print hash(x)
    print "---------"
    x = puzzle.move(7)
    print x
    print hash(x)
    print "---------"
    x = puzzle.move(2)
    print x
    print hash(x)

