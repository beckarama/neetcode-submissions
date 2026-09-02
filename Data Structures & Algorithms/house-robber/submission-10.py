class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = nums[i]
            nums[i] = max(nums[i - 1], nums[i - 2] + temp)
        return nums[-1]
        
