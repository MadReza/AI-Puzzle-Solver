"""
    Used as reference: http://codereview.stackexchange.com/a/76949
"""

class Puzzle:
    width = 3  # TODO: currently for 8 puzzle. Change algo for bigger later.
    #Using math.sqrt(board) to check if valid board for future use
    hole_position = 0
    
    def __init__(self, board):
        self.board = board
        self.hole_position = board.index(0)

    def __str__(self):
        return "\n".join(str(self.board[start : start + self.width])
		for start in range(0, len(self.board), self.width))

    """
        Unique hash created by XOR of value and position on board
    """
    def __hash__(self):
        h = 0
        for i, value in enumerate(self.board):
            h ^= value << i
        return h

    def __eq__(self, other):
        return self.board == other.board

    """
        Expected solution is the empty spot to be at bottom right
        Expecting:
            1 2 3
            4 5 6
            7 8 0
    """    
    def solved(self):
        return self.board == range(1,9) + [0] #TODO change to expandable board

    def possible_moves(self):
        moves = []
        # Up, down
        for dest in (self.hole_position - self.width, self.hole_position + self.width):
            if 0 <= dest < len(self.board):
                moves.append(dest)
        # Left, right
        for dest in (self.hole_position - 1, self.hole_position + 1):
            if dest // self.width == self.hole_position // self.width:
                moves.append(dest)
        return moves

    def move(self, destination):
        board = self.board[:] #deep copy
        if destination not in self.possible_moves():
            raise AttributeError('destination is outside allowed moves', 'destination: ' + `destination`, 'Allowed: ' + `self.possible_moves()`)
        board[self.hole_position], board[destination] = board[destination], board[self.hole_position]
        return Puzzle(board)









        
