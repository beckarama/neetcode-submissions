class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        s1_count = [0] * 26
        for c in s1:
            idx = ord(c) - ord('a')
            s1_count[idx] += 1
        
        L = 0
        sub_s = [0] * 26
        for R in range(len(s2)):
            if (R - L + 1) > n:
                L_idx = ord(s2[L]) - ord('a')
                sub_s[L_idx] -= 1
                L += 1

            R_idx = ord(s2[R]) - ord('a')
            sub_s[R_idx] += 1

            if sub_s == s1_count:
                return True
        return False

