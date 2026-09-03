class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        res = 0

        L = 0
        for R, char in enumerate(s):
            if char in last_seen:
                L = max(L, last_seen[char] + 1)
            last_seen[char] = R
            res = max(res, R - L + 1)
        return res
        