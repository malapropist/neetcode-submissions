class Solution:
    # [4,5,6,1,2,3]
    # [6,1,2,3,4,5]
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        smallest = 1000
        while l <= r:
            mid = (l+r)//2
            if nums[mid]<smallest:
                    smallest = nums[mid]
            if nums[mid] <= nums[mid-1]:
                return smallest
            if nums[mid]>=nums[-1]:
                l = mid+1
            elif nums[mid]<=nums[-1]:
                r = mid-1
            