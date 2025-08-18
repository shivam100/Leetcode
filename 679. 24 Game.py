# https://leetcode.com/problems/24-game/description/?envType=daily-question&envId=2025-08-18

# Thought Process:
# I am thinking of trying backtracking to try all combination of the numbers and operators.

from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6 # because the division is float 
            n = len(nums)
            for i in range(n): # Take first number
                for j in range(i+1,n): # take second number
                    a,b = nums[i], nums[j]
                    rest = [nums[k] for k in range(n) if k != i and k != j] # rest of the numbers
                    # Try all combinations of operations
                    candidates = [a+b, a-b, b-a, a*b]
                    if abs(b) > 1e-6:
                        candidates.append(a/b)
                    if abs(a) > 1e-6:
                        candidates.append(b/a)
                    # Try all candidates and result of operations
                    for c in candidates:
                        if backtrack(rest + [c]):
                            return True
            return False
        
        return backtrack(cards)
        

Sol = Solution()
assert Sol.judgePoint24([4, 1, 8, 7]) == True
assert Sol.judgePoint24([1, 2, 1, 2]) == False
