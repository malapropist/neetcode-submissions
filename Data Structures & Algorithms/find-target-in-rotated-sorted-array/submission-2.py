class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        spot = 0
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<nums[spot]:
                spot = mid
            if nums[l]>nums[r]:
                l = mid+1
            else:
                r = mid-1

        print(spot)
        print(nums)
        if spot!=0:  
            nums = nums[spot:len(nums)]+nums[0:spot]
        print(nums)
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            elif nums[mid]==target:
                return (mid+spot)%len(nums)
        return -1
            
