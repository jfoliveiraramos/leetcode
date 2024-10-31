from typing import List
from bisect import bisect_left

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        size = len(nums)
        left = [0] * size
        right = [0] * size
        
        dp = []
        for i in range(size):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            left[i] = len(dp)

        print(dp)
        
        dp = []
        for i in range(size - 1, -1, -1):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            left[i] = len(dp)
        
        maxSize = 0
        for i in range(size):
            if left[i] > 1 and right[i] > 1:
                maxSize = max(maxSize, left[i] + right[i])
        
        return size - maxSize + 1 

