class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        res = []

        for num in hash_map:
            val = num
            seq = []
            seq.append(val)

            while val+1 in hash_map:
                seq.append(val+1)
                val +=1

            if len(seq) > len(res):
                res = seq
        return len(res)

