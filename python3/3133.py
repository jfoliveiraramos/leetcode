class Solution:
    def minEnd(self, n: int, x: int) -> int:

        res = x
        mask = 1
        n = n - 1
        i = 0
        
        while n:
            if not (x & mask):
                res |= (n & 1) << i
                x |= mask
                n >>= 1
            mask <<= 1
            i += 1

        return res
