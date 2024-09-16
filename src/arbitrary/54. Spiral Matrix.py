# accepted in first attempt

from typing import List, Tuple
from enum import Enum


class DIRECTION(Enum):
    RIGHT = (+0, +1)
    DOWN = (+1, +0)
    LEFT = (+0, -1)
    UP = (-1, +0)


class Solution:
    def getNextDirection(self, currDir: DIRECTION) -> DIRECTION:
        nextDir = currDir

        if currDir == DIRECTION.RIGHT:
            nextDir = DIRECTION.DOWN
        elif currDir == DIRECTION.DOWN:
            nextDir = DIRECTION.LEFT
        elif currDir == DIRECTION.LEFT:
            nextDir = DIRECTION.UP
        elif currDir == DIRECTION.UP:
            nextDir = DIRECTION.RIGHT

        return nextDir

    def getNextPointer(self, currRow: int, currCol: int, currDir: DIRECTION) -> Tuple[int]:
        rowUpdater, colUpdater = currDir.value

        return (currRow + rowUpdater, currCol + colUpdater)

    def isValidPointer(self, newRow, newCol, rows, cols, visited: List[List[bool]]) -> bool:
        isValid = False
        if -1 < newRow < rows and -1 < newCol < cols:
            if not visited[newRow][newCol]:
                isValid = True

        return isValid

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        currRow, currCol = 0, 0
        currDir = DIRECTION.RIGHT
        result = []
        visited = [[False] * cols for _ in range(rows)]

        while len(result) < rows * cols:
            result.append(matrix[currRow][currCol])
            visited[currRow][currCol] = True

            newRow, newCol = self.getNextPointer(currRow, currCol, currDir)

            if self.isValidPointer(newRow, newCol, rows, cols, visited):
                currRow, currCol = newRow, newCol
            else:
                currDir = self.getNextDirection(currDir)
                currRow, currCol = self.getNextPointer(currRow, currCol, currDir)

        return result
