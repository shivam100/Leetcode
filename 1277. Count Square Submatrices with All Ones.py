# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20
# Thought Process : Need to use a 2D DP here
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0] * n for a in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j] , dp[i][j-1], dp[i-1][j-1]) + 1
                ans +=  dp[i][j]
        return ans

sol = Solution()
assert(sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) == 15
assert(sol.countSquares([[1,0,1],[1,1,0],[1,1,0]])) == 7
