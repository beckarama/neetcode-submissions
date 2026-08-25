class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x,y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(minHeap, [distance, x, y])

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res


        