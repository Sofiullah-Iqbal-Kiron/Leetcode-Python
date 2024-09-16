from typing import List
from enum import Enum


class DIRECTION(Enum):
    # RDLU
    RIGHT = (+0, +1)
    DOWN = (+1, +0)
    LEFT = (+0, -1)
    UP = (-1, +0)


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        currRow, currCol = rStart, cStart
        currDir = DIRECTION.RIGHT
        result = []
        result.append([currRow, currCol])

