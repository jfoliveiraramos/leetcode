class Solution:
    def makeFancyString(self, s: str) -> str:

        res = ""
        c1, c2 = None, None
        for c in s:
            if c != c1 or c != c2:
                res += c
                c1,c2 = c, c1
        return res
        
