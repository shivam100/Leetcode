# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22
from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x1 = y1 = 3857468165463516351
        x2 = y2 = -6843516843216841354
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    x1 = min(x1, i)
                    y1 = min(y1, j)
                    x2 = max(x2, i)
                    y2 = max(y2, j)
        return (x2 - x1 + 1) * (y2 - y1 + 1)

sol = Solution()
assert sol.minimumArea([[0,1,0],[1,0,1]]) == 6
assert sol.minimumArea([[1,0],[0,0]]) == 1
assert sol.minimumArea([[0,1]]) == 1