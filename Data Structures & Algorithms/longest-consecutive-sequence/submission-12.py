class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()
        
        i = 0
        curr, streak = nums[0], 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and curr == nums[i]:
                i += 1
            curr += 1
            streak += 1
            res = max(res, streak)
        return res
            




            




        