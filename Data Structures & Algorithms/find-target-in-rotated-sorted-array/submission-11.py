class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[mid]>nums[-1]:
                l = mid+1
            else:
                r = mid-1
        pivot = l

        if nums[-1]>=target:
            l=pivot
            r = len(nums)-1
        else:
            l = 0
            r = pivot

        while l <= r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else: r = mid-1

        return -1