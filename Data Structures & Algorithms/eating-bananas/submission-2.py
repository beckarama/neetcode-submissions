class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        #[1, 2, 3, 4]

        while l < r:
            mid = (l + r) // 2
            hours = sum((p + mid - 1) // mid for p in piles)
            
            if hours > h:
                l = mid + 1
            else:
                r = mid
        return l


        