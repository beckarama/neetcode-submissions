class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        i = j = 0

        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        
        if len(word1) > len(word2):
            return res + word1[i:]
        else:
            return res + word2[j:]
        
        return res

        