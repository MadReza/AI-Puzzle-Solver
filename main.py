import argparse

def getCmdArgs():
    """Helper function for analyzing arguments"""
    parser = argparse.ArgumentParser(description='Puzzle Solver')
    parser.add_argument(
        '-a',
        action="store",
        dest="algorithm",
        choices=["a*", "best", "bfs", "dfs"],
        default="a*",
        help='Selected algorithm to solve Puzzle. Default: A*'
    )

    parser.add_argument(
        '-p',
        action="store",
        dest="thePuzzle",
        metavar='N',
        type=int,
        nargs=8,
        help="The 8-puzzle required to be solved. 0 being the empty spot. e.g.: 1 2 3 4 0 8 7 6 5"
    )    
    
    return parser.parse_args()

args = getCmdArgs()


if __name__ == '__main__':
    print dir()
    print args.algorithm
