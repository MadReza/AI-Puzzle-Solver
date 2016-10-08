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
        '-he',
        action="store",
        dest="heuristic",
        choices=["manhattan", "misplaced", "min"],
        default="min",
        help='Selected heuristic to solve Puzzle. Default: Min'
    )

    parser.add_argument(
        '-p',
        action="store",
        dest="thePuzzle",
        metavar='N',
        type=int,
        nargs=9,
        default=[1,2,3,4,0,5,6,7,8],
        help="The 8-puzzle required to be solved. 0 being the empty spot. e.g.: 1 2 3 4 0 8 7 6 5"
    )    
    
    return parser.parse_args()
