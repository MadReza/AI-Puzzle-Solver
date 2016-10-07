from Puzzle import Puzzle
"""
    Assuming the Goal puzzle is having the empty at bottom right
    up and down movement cost puzzle.width
    left and right movement cost 1
"""
def Manhattan_Distance(puzzle):
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
