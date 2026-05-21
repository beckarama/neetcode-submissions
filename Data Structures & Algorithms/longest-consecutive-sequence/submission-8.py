class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        longest = 0
        for num in nums:
            if num-1 in set_nums:
                continue
            
            val = num
            temp = 1
            while val + 1 in set_nums:
                temp+=1
                val+=1
            longest = max(longest, temp)
        return longest
                

        