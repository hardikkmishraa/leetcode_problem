
from collections import deque
from copy import deepcopy

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        if image[sr][sc] == color:
            return image

        visited = deepcopy(image)

        rows = len(visited)
        cols = len(visited[0])

        initial_color = visited[sr][sc]

        queue = deque()
        queue.append((sr, sc))

        # Mark starting cell immediately
        visited[sr][sc] = color

        while queue:
            i, j = queue.popleft()

            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_i = i + x
                new_j = j + y

                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                if visited[new_i][new_j] != initial_color:
                    continue

                # Mark before adding to queue
                visited[new_i][new_j] = color
                queue.append((new_i, new_j))

        return visited
