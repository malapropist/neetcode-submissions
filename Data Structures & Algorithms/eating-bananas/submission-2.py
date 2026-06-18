class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        best = r
        while l<=r:
            time = 0
            speed = (l+r)//2
            for i in piles:
                time += -(-i//speed)
            if time > h:
                l = speed + 1
            else:
                best = min(best,speed)
                r = speed - 1
        return best