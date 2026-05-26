class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}

        L = 0
        max_f = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            max_f = max(max_f, count[s[R]])
            
            while (R - L + 1) - max_f > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res