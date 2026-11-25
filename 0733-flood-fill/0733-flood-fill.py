
# from copy import deepcopy
# from typing import List

#usnig dfs with recursion

class Solution:
    def dfs(self, i, j, new_color, initial_color, visited, rows, cols):

        if i < 0 or i >= rows or j < 0 or j >= cols:
            return

        if visited[i][j] != initial_color:
            return

        visited[i][j] = new_color

        self.dfs(i+1, j, new_color, initial_color, visited, rows, cols)
        self.dfs(i-1, j, new_color, initial_color, visited, rows, cols)
        self.dfs(i, j+1, new_color, initial_color, visited, rows, cols)
        self.dfs(i, j-1, new_color, initial_color, visited, rows, cols)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        visited = deepcopy(image)

        rows = len(visited)
        cols = len(visited[0])

        initial_color = visited[sr][sc]

        self.dfs(sr, sc, color, initial_color, visited, rows, cols)

        return visited
