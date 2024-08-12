# not accepted

from typing import List


class Solution:
    visited = []

    def dfs(self, grid: List[List[int]], i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or self.visited[i][j] or grid[i][j] == 0:
            return

        self.visited[i][j] = True

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numberOfIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        self.visited = [[False]*cols]*rows

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not self.visited[i][j]:
                    self.dfs(grid, i, j)
                    islands += 1

        return islands

    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        islands = self.numberOfIslands(grid)
        if islands > 1 or islands == 0:
            return 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    islands = self.numberOfIslands(grid)
                    if islands > 1 or islands == 0:
                        return 1
                    grid[i][j] = 1

        return 2
