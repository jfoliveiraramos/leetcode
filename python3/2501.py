from typing import List
from collections import defaultdict

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums = sorted(nums)

        nums_set = set(nums)

        max_streak = -1

        for num in nums:
            streak = 0
            curr = num

            while curr in nums_set:
                streak += 1
                nums_set.remove(curr)
                curr = curr**2
            if streak > 1:
                max_streak = max(max_streak, streak)

        return max_streak
