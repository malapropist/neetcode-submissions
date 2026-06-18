class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ar = {}
        for i in nums:
            if i not in ar:
                ar[i] = 1
            else:
                return True
        return False
