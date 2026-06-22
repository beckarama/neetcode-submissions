class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_len = 0
        
        L = 0
        window_sum = 0

        for R in range(len(nums)):
            window_sum += nums[R]

            while window_sum >= target:
                if not max_len:
                    max_len = R - L + 1
                else:
                    max_len = min(max_len, R - L + 1)
                window_sum -= nums[L]
                L += 1
        return max_len
        