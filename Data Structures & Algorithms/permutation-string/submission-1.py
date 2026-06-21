class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        s1_count = [0] * 26
        for c in s1:
            idx = ord(c) - ord('a')
            s1_count[idx] += 1
        
        L = 0
        window_count = [0] * 26

        for R in range(len(s2)):
            window_count[ord(s2[R]) - ord('a')] += 1

            if R - L + 1 > n:
                window_count[ord(s2[L]) - ord('a')] -= 1
                L += 1

            if window_count == s1_count:
                return True
        return False

