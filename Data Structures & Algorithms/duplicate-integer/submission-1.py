class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        library = {}
        for i in nums:
            if i in library:
                return True
            else:
                library[i] = 1
        return False