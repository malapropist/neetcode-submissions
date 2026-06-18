class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lib = {}
        for pos, i in enumerate(nums):
            if i in lib:
                return [lib[i], pos]
            else:
                lib[target-i] = pos