class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            print(i, abs(i),nums[abs(i)], nums)
            if nums[abs(i)]<0:
                return abs(i)
            else:
                nums[abs(i)]*=-1
        return 'nah'
