class Solution:
    def compressedString(self, word: str) -> str:

        marker = 0
        res = ""
        for i in range(1,len(word)):
            if word[i] != word[i - 1] or i - marker == 9:
                res += f"{i - marker}{word[i - 1]}" 
                marker = i
        res += f"{len(word) - marker}{word[-1]}" 

        return res
        
        
