class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle empty input
        if not matrix or not matrix[0]:
            return []

        result = []                           # stores the spiral order

        # Initialize boundary pointers
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        # Continue until the boundaries cross
        while top <= bottom and left <= right:
            # Traverse the top row from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1                          # top row is done

            # Traverse the right column from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1                        # right column is done

            # Traverse the bottom row from right to left (if any)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1                   # bottom row is done

            # Traverse the left column from bottom to top (if any)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1                     # left column is done

        return result