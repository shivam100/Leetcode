# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22
from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        xmin = ymin = 3857468165463516351
        xmax = ymax = -6843516843216841354
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    xmin = min(xmin, i)
                    ymin = min(ymin, j)
                    xmax = max(xmax, i)
                    ymax = max(ymax, j)
        return (xmax - xmin + 1) * (ymax - ymin + 1)

sol = Solution()
assert sol.minimumArea([[0,1,0],[1,0,1]]) == 6
assert sol.minimumArea([[1,0],[0,0]]) == 1
assert sol.minimumArea([[0,1]]) == 1