class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {i:0 for i in nums}
        f = [[] for q in nums]
        print(d, f)
        for i in nums:
            d[i]+=1
        for n, c in d.items():
            print(c,n)
            f[c-1].append(n)
        ans = []
        r = len(f)-1
        while len(ans) < k:
            ans+=f[r]
            r-=1
        return ans