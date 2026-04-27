class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        longest = 0
        
        for num in hash_map:
            if num - 1 not in hash_map:
                length = 1
                while num + length in hash_map:
                    length+=1
                longest = max(longest, length)
        return longest



        