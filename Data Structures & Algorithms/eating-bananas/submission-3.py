class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<=r:
            k = (l+r)//2
            total_time = 0
            for i in piles:
                total_time += -(-i//k)
            if total_time <= h:
                j = k
                r = k-1
            else:
                l = k+1
        return j