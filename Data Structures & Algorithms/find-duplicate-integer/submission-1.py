class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setty = set()
        for i in nums:
            if i in setty:
                return i
            else:
                setty.add(i)
        