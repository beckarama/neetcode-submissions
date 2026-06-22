class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        
        L = 0
        window_sum = 0

        for R in range(len(nums)):
            window_sum += nums[R]

            while window_sum >= target:
                min_len = min(min_len, R - L + 1)
                window_sum -= nums[L]
                L += 1

        return min_len if min_len != float('inf') else 0
        