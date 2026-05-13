class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)

        longest = 0
        for num in hash_map:
            print(f"{num}")
            if num-1 not in hash_map:
                val = num + 1
                temp = 1
                while val in hash_map:
                    print(f"{val=}, {temp=}")
                    val += 1
                    temp += 1

                longest = max(longest, temp)
        return longest