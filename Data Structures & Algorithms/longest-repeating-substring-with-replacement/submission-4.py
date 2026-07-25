class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        L = 0
        most_freq = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            most_freq = max(most_freq, count[s[R]])

            while (R - L + 1) - most_freq > k:
                count[s[L]] -= 1
                L += 1
            
            res = max(res, (R - L + 1))
        return res

            
