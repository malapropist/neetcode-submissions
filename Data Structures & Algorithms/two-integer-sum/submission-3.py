class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {target-n:pos for pos,n in enumerate(nums)}
        for j,i in enumerate(nums):
            if i in d and j != d[i]:
                return [j,d[i]]