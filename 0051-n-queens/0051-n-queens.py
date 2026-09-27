class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        # Base case: placed all queens successfully
        if col == n:
            ans.append(board[:])  # Make a copy of current board
            return

        # Try each row in current column
        for row in range(n):
            # O(1) safety check using our tracking arrays
            if (
                leftrow[row] == 0
                and lowerDiagonal[row + col] == 0
                and upperDiagonal[n - 1 + col - row] == 0
            ):
                # Place queen and update all tracking arrays
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                leftrow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1
                
                # Recurse to next column
                self.solve(
                    col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n
                )
                
                # Backtrack: remove queen and reset tracking arrays
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                leftrow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        
        # Initialize tracking arrays
        leftrow = [0] * n  # Track occupied rows
        upperDiagonal = [0] * (2 * n - 1)  # Track upper diagonals
        lowerDiagonal = [0] * (2 * n - 1)  # Track lower diagonals
        
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans