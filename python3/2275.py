from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        combination = 0
        mask = 1

        for i in range(24):
            ones = 0
            for cand in candidates:
                ones += 1 if mask & cand else 0
            combination = max(combination, ones)
            mask <<= 1
        
        return combination
        
