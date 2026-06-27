class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        
        L = 0
        zero_count = 0
        for R in range(len(nums)):
            if nums[R] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[L] == 0:
                    zero_count -= 1
                L += 1
            res = max(res, (R - L + 1))
        return res
        