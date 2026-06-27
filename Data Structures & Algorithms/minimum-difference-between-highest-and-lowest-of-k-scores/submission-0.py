class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = float('inf')
        L = 0
        for R in range(len(nums)):
            if (R - L + 1) == k:
                res = min(res, nums[R] - nums[L])
                L += 1
        return res