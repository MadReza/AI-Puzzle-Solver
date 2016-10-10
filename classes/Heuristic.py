from Puzzle import Puzzle


def get_heuristic_function(heuristic):
    if heuristic == "manhattan":
        return manhattan_distance
    if heuristic == "misplaced":
        return misplaced
    if heuristic == "min":
        return min
    if heuristic == "linear":
        return linear_conflict
    if heuristic == "nilsson":
        return nilsson
    return None

def get_heuristic_name(heuristic):
    if heuristic == "manhattan":
        return "Manhattan Distance"
    if heuristic == "misplaced":
        return "Misplaced"
    if heuristic == "min":
        return "Min(Manhattan, Misplaced)"
    if heuristic == "linear":
        return "Linear Conflict"
    if heuristic == "nilsson":
        return "Nilsson"
    return None


"""
    Assuming the Goal puzzle is having the empty at bottom right
    up and down movement cost puzzle.width
    left and right movement cost 1
	------
	Logic might be a hard but test it out, it works ^^. TODO: cleaning
"""
def manhattan_distance(puzzle):
    steps = 0

    for pos, val in enumerate(puzzle.board):
        goal = (val - 1) % len(puzzle.board) #rotate 0 to bot right
        dist = abs(goal - pos)

        #add Up and Down movements
        while dist >= puzzle.width:
            steps += 1
            dist -= puzzle.width

        #add Left and right movements
        steps += dist
        
    return steps

"""
    Todo: Nilsson's sequence score.
    Inadmissible
"""
def nilsson(puzzle):
    steps = 0

    goal = [1,2,3,8,0,4,7,6,5]
    for pos, val in enumerate(puzzle.board):
        if goal[pos] != val:
            steps = steps + 2

    #middle not open
    if puzzle.board[4] != 0:
        steps = steps + 1
    
    return manhattan_distance(puzzle) + steps

"""
Linear Conflicts occuring in same row or same col
Each conflict is + 2 steps
+ Manhattan is the total steps required.
"""
def linear_conflict(puzzle):
    floor = 0
    ceil = puzzle.width
    steps = 0

    #check row conflicts
    while ceil <= len(puzzle.board):
        for pos in range(floor, ceil):
             x = (puzzle.board[pos] - 1) % len(puzzle.board)    #0 is last position
             if floor <= x < ceil:
                 for new_pos in range(x+1, ceil):
                     y = (puzzle.board[new_pos] - 1) % len(puzzle.board)
                     if x > y:
                         #conflict
                         steps = steps + 2
        floor += puzzle.width
        ceil += puzzle.width

    #check column conflicts
    col = 0
    while col < puzzle.width:
        row = 0
        while row < puzzle.width:
            pos = col + row * puzzle.width
            val = (puzzle.board[pos] - 1) % len(puzzle.board)  #again because 0 is expected to be bottom right

            if (val % puzzle.width) == col:
                next_row = row + 1
                while next_row < puzzle.width:
                    next_pos = col + next_row * puzzle.width
                    next_val = (puzzle.board[next_pos] - 1) % len(puzzle.board)
                    if val < next_val and (next_val % puzzle.width) == col:
                        steps = steps + 2
                    next_row = next_row + 1
            row = row + 1
        col = col + 1
            
    return manhattan_distance(puzzle) + steps

def misplaced(puzzle):
    wrong_place = 0

    for pos, val in enumerate(puzzle.board):
        if pos != ((val-1)%len(puzzle.board)):
            wrong_place += 1
            
    return wrong_place

def min(puzzle):
    mp = misplaced(puzzle)
    man = manhattan_distance(puzzle)
    if mp < man:
        return mp
    return man
