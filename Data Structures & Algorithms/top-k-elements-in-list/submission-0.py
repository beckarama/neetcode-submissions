class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        res = []

        for v in nums:
            frequency[v] = frequency.get(v,0) + 1
        
        for _ in range(k):
            max_num = max(frequency, key=frequency.get)
            res.append(max_num)
            frequency.pop(max_num)
        return res


        