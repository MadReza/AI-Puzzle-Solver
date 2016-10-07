class Puzzle:
    width = 3  # TODO: currently for 8 puzzle. Change algo for bigger later.
    #Using math.sqrt(board) to check if valid board for future use
    
    def __init__(self, board):
        self.board = board

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
        

