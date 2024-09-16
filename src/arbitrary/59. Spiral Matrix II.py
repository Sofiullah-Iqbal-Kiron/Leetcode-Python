from typing import List, Tuple
from enum import Enum


class DIRECTION(Enum):
    RIGHT = (+0, +1)  # col++
    DOWN = (+1, +0)  # row++
    LEFT = (+0, -1)  # col--
    UP = (-1, +0)  # row--


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

    def getNextPointer(self, currRow, currCol, currDir: DIRECTION) -> Tuple[int]:
        rowUpdater, colUpdater = currDir.value

        return (currRow + rowUpdater, currCol + colUpdater)

    def isValidPointer(self, newRow, newCol, rows, cols, result):
        isValid = False

        if -1 < newRow < rows and -1 < newCol < cols:
            if result[newRow][newCol] == -1:
                isValid = True

        return isValid

    def generateMatrix(self, n: int) -> List[List[int]]:
        currRow, currCol = 0, 0
        currDir = DIRECTION.RIGHT
        currVal = 1
        result = [[-1 for _ in range(n)] for _ in range(n)]

        while currVal <= n * n:
            result[currRow][currCol] = currVal
            newRow, newCol = self.getNextPointer(currRow, currCol, currDir)

            if self.isValidPointer(newRow, newCol, n, n, result):
                currRow, currCol = newRow, newCol
            else:
                currDir = self.getNextDirection(currDir)
                currRow, currCol = self.getNextPointer(currRow, currCol, currDir)

            currVal += 1

        return result
