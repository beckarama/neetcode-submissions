class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n

        for i in range(n - 1):
            if i == 0:
                prefix[i + 1] = nums[i]
            else:
                prefix[i + 1] = prefix[i] * nums[i]
        
        for i in range(n - 1, 0, -1):
            if i == n - 1:
                suffix[i - 1] = nums[i]
            else:
                suffix[i - 1] = suffix[i] * nums[i]

        res[0] = suffix[0]
        res[-1] = prefix[-1]

        for i in range(1, n - 1):
            res[i] = prefix[i] * suffix[i]

        return res
        
        
        