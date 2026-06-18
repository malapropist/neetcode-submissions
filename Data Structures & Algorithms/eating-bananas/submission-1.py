class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            time = 0
            print(l, mid, r)
            for o in piles:
                time += -(o//-mid)
            if time > h:
                l = mid+1
            elif time <= h:
                ans = mid
                r = mid-1
        return ans
