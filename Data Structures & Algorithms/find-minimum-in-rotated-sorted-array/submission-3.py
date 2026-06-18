class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = nums[0]
        if nums[r]>=nums[l]:
            return ans
        while r >= l:
            mid =(r+l)//2
            if nums[r]>nums[l]:
                ans=min(ans,nums[mid])
                r = mid-1
            else:
                ans=min(ans,nums[mid])
                l = mid+1
        return ans