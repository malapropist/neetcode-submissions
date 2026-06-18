class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        g = set()
        for i in nums:
            if i in g:
                return True
            else:
                g.add(i)
        return False
