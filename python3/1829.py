from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        ans = []
        acc = 0
        max_n = (1 << maximumBit) - 1

        for num in nums:
            acc ^= num
            ans.append(acc ^ max_n)

        return ans[::-1]
