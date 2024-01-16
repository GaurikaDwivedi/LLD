class TicTacToe:
    def __init__(self, n):
        self.grid = [[0]*n for _ in range(n)]

    def move(self, row, col, player):
        if row >= len(self.grid) or col >= len(self.grid):
            return 0
        self.grid[row][col] = 1 if player == 1 else 2
        if self._checkVerticalWin(col, player):
            return player
        if self._checkHorizontalWin(row, player):
            return player
        if self._checkDiagonalWin(row, col, player):
            return player
        if self._checkAntiDiagonalWin(row, col, player):
            return player
        return 0

    def _checkVerticalWin(self, col, player):
        i = 0
        while i < len(self.grid):
            if self.grid[i][col] != player:
                return False
            i += 1
        return True

    def _checkHorizontalWin(self, row, player):
        j = 0
        while j < len(self.grid):
            if self.grid[row][j] != player:
                return False
            j += 1
        return True

    def _checkDiagonalWin(self, row, col, player):

        if row != col:
            return False
        topLeftToBottomRight = True
        i = 0
        while i < len(self.grid):
            if self.grid[i][i] != player:
                topLeftToBottomRight = False
            i += 1
        return topLeftToBottomRight

    def _checkAntiDiagonalWin(self, row, col, player):
        if row + col != len(self.grid) - 1:
            return False
        topRightToBottomLeft = True
        columnIndex = 0
        while columnIndex < len(self.grid):
            rowIndex = len(self.grid) - 1 - columnIndex
            if self.grid[columnIndex][rowIndex] != player:
                topRightToBottomLeft = False
            columnIndex += 1
        return topRightToBottomLeft
    
def main():
    # Create an instance of TicTacToe with a dimension of 3 (3x3 grid)
    tic_tac_toe = TicTacToe(3)

    # Simulate moves
    moves = [(0, 0), (1, 1), (0, 1), (2, 2), (0, 2)]
    
    current_player = 1

    for move in moves:
        row, col = move
        winner = tic_tac_toe.move(row, col, current_player)
        

        if winner != 0:
            print(f"Player {winner} wins!")
            break

        # Switch to the other player for the next move
        current_player = 3 - current_player  # Alternates between players 1 and 2

    else:
        print("The game ended in a draw.")

if __name__ == "__main__":
    main()