class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        res_len = float('inf')

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        count_window = {}

        have = 0
        need = len(count_t)

        L = 0
        for R in range(len(s)):
            if s[R] in count_t:
                count_window[s[R]] = count_window.get(s[R], 0) + 1

                if count_window[s[R]] == count_t[s[R]]:
                    have += 1
            
            while have == need:
                if R - L + 1 < res_len:
                    res_len = R - L + 1
                    res = s[L:R+1]
        
                if s[L] in count_t:
                    count_window[s[L]] -= 1
                    if count_window[s[L]] < count_t[s[L]]:
                        have -= 1
                L += 1
        return res
        