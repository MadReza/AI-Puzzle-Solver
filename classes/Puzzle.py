class Puzzle:
    width = 3  # TODO: currently for 8 puzzle. Change algo for bigger later.
    
    def __init__(self, board):
        self.board = board

    def __str__(self):
        return "\n".join(str(self.board[start : start + self.width])
		for start in range(0, len(self.board), self.width))
