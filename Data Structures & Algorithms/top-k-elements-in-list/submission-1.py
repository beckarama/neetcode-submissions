class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for val, cnt in count.items():
            buckets[cnt].append(val)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res





        
