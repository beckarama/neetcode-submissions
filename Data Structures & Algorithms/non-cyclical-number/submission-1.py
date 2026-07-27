class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = 0
        
        while res != 1:
            res = 0
            for val in str(n):
                res += int(val) ** 2 
            
            if res in seen:
                return False
            seen.add(res)
            n = res
        return True