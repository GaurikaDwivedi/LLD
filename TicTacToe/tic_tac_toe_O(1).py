class TicTacToe:

    def __init__(self, n):
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.rowSum = [0 for _ in range(n)]
        self.colSum = [0 for _ in range(n)]
        self.diagonalSum = 0
        self.antiDiagonalSum = 0
        self.dimension = n

    def move(self, row, col, player):
        value = 'X' if player == 1 else 'O'
        self.board[row][col] = value
        self.rowSum[row] += 1 if player == 1 else -1
        self.colSum[col] += 1 if player == 1 else -1
        if row == col:
            self.diagonalSum += 1 if player == 1 else -1
        if col == self.dimension - row - 1:
            self.antiDiagonalSum += 1 if player == 1 else -1
        """for the player to win by making this move
        summation of all values in the cells at row index = row must be equal to the dimension
        or 
        summation of all values in the cells at column index = col must be equal to the dimension
        or 
        summation of all values in the cells located on the diagonal must be equal to the dimension
        or 
        summation of all values in the cells located on the anti-diagonal must be equal to the dimension"""
        if abs(self.rowSum[row]) == self.dimension or abs(self.colSum[col]) == self.dimension or abs(
                self.diagonalSum) == self.dimension or abs(self.antiDiagonalSum) == self.dimension:
            return player
        return 0
    
    def display_board(self):
        for row in self.board:
            print('|'.join(row))
        print()
    
def main():
    # Create an instance of TicTacToe with a dimension of 3 (3x3 grid)
    tic_tac_toe = TicTacToe(3)

    # Simulate moves
    moves = [(0, 0), (1, 1), (0, 1), (2, 2), (0, 2)]
    
    current_player = 1

    for move in moves:
        row, col = move
        winner = tic_tac_toe.move(row, col, current_player)
        tic_tac_toe.display_board()

        if winner != 0:
            print(f"Player {winner} wins!")
            break

        # Switch to the other player for the next move
        current_player = 3 - current_player  # Alternates between players 1 and 2

    else:
        print("The game ended in a draw.")

if __name__ == "__main__":
    main()