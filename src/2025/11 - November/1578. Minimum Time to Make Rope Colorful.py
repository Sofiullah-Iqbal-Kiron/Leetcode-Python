# Accepted at second attempt.

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, n, ans = 1, len(colors), 0

        while i < n:
            if colors[i - 1] == colors[i]:
                cmax = neededTime[i - 1]
                windowSum = cmax
                while i < n and colors[i - 1] == colors[i]:
                    cmax = max(cmax, neededTime[i])
                    windowSum += neededTime[i]
                    i += 1
                ans += windowSum - cmax
            i += 1

        return ans
