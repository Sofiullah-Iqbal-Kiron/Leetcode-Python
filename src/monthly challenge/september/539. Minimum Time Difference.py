# accepted in first attempt

from typing import List


class Solution:
    def getMinutes(self, time: str) -> int:
        time = time.split(":")
        hh = int(time[0]) * 60
        mm = int(time[1])

        return hh + mm

    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            timePoints[i] = self.getMinutes(timePoints[i])

        timePoints.sort()

        ans = min(timePoints[i + 1] - timePoints[i] for i in range(len(timePoints) - 1))

        return min(ans, 24 * 60 - timePoints[-1] + timePoints[0])
