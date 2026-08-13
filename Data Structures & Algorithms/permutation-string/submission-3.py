class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        w_freq = [0] * 26
        L = 0
        for R in range(len(s2)):
            w_freq[ord(s2[R]) - ord('a')] += 1
            
            if R - L + 1 > len(s1):
                w_freq[ord(s2[L]) - ord('a')] -= 1
                L += 1
            
            if w_freq == s1_freq:
                return True
        return False