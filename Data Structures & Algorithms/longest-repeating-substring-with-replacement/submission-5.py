class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        L = 0
        window_max = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            window_max = max(window_max, count[s[R]])

            while (R - L + 1) - window_max > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res