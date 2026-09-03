class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        res = 0
        for num in nums:
            if num - 1 not in seen:
                seq = num
                length = 1
                while seq + 1 in seen:
                    length += 1
                    seq += 1
                res = max(res, length)

        return res



        