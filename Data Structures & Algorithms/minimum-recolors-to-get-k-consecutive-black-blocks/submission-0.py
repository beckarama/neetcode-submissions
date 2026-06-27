class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')

        L = 0
        window_sum = 0
        for R in range(len(blocks)):
            if blocks[R] == "W":
                window_sum += 1
            
            if (R - L + 1) == k:
                res = min(res, window_sum)
                
                if blocks[L] == "W":
                    window_sum -= 1
                L += 1
        return res

        