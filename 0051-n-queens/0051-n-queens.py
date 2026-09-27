class Solution:
    def isSafe1(self, row, col, board, n):
        duprow = row
        dupcol = col

        # Check upper-left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Reset and check left row
        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1

        # Reset and check lower-left diagonal
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        
        return True

    def solve(self, col, board, ans, n):
        # Base case: placed queens in all columns
        if col == n:
            ans.append(list(board))  # Make a copy of current board state
            return

        # Try placing queen in each row of current column
        for row in range(n):
            if self.isSafe1(row, col, board, n):
                # Place queen: replace '.' with 'Q' at position (row, col)
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                
                # Recursively solve for next column
                self.solve(col + 1, board, ans, n)
                
                # Backtrack: remove queen by replacing 'Q' with '.'
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]  # Initialize n×n board with dots
        self.solve(0, board, ans, n)  # Start from column 0
        return ans