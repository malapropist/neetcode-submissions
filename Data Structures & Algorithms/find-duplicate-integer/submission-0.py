class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        library = set()
        for i in nums:
            if i in library:
                return i
            else:
                library.add(i)