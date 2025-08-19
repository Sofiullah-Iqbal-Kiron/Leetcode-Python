from typing import List


class Solution:
    """
    unguarded -> 0
    guarded -> 1
    guard -> 2
    wall -> 3
    """

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unguarded = m * n
        matrix = [[0] * n for _ in range(m)]

        # guards marking and reducing unguarded
        for guard in guards:
            row = guard[0]
            col = guard[1]
            matrix[row][col] = 2
            unguarded -= 1

        # walls marking and reducing unguarded
        for wall in walls:
            row = wall[0]
            col = wall[1]
            matrix[row][col] = 3
            unguarded -= 1
        
        for i in range(m):
            for j in range(n):
                pass
