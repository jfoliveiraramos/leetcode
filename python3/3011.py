from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        max_n = 0
        curr_max = nums[0]

        for i in range(1,len(nums)):

            if bin(nums[i-1]).count('1') == bin(nums[i]).count('1'):
                curr_max = max(curr_max, nums[i])
            else:
                max_n = curr_max
                curr_max = nums[i]

            if nums[i] < max_n:
                return False

        return True
            
        
