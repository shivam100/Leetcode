# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/?envType=daily-question&envId=2025-08-19

# Thought Process:
# I am thinking of using a two-pointer approach to find contiguous subarrays of zeros.
# For each contiguous segment of zeros, the number of zero-filled subarrays can be calculated using the formula n * (n + 1) // 2,
# where n is the length of the segment.

from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        conitgous_zero_count = []
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != 0  and nums[right] != 0:
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
            else:
                if nums[left] == 0:
                    conitgous_zero_count.append(right - left)
                left = right
                right += 1
        
        if nums[left] == 0:
            conitgous_zero_count.append(right - left)
        
        contigous_zero_sum = 0
        for x in conitgous_zero_count:
            contigous_zero_sum += (x * (x + 1)) // 2
        return contigous_zero_sum

sol = Solution()
# print(sol.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4])) # Expected output: [2, 2]
assert sol.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
assert sol.zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9