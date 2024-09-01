from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        iterator = 0

        if len(original) != m * n:
            return ans

        for i in range(m):
            newArr = []
            for j in range(n):
                newArr.append(original[iterator])
                iterator += 1
            ans.append(newArr)

        return ans
