class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        L = 0
        maxHeap = []
        for R in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[R], R))
            
            if R - L + 1 == k:
                max_val, idx = maxHeap[0] # (2, 1)
                
                while idx < L:
                    heapq.heappop(maxHeap)
                    max_val, idx = maxHeap[0]

                res.append(-max_val)
                L += 1
        return res
        