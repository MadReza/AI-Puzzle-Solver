from Puzzle import Puzzle
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

def misplaced(puzzle):
    wrong_place = 0

    for pos, val in enumerate(puzzle.board):
        if pos != ((val-1)%len(puzzle.board)):
            wrong_place += 1
            
    return wrong_place
