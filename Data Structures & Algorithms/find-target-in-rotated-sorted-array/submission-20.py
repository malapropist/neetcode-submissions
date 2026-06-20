class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        #left half?
        split=target<nums[0]
        #find rotation point
        while l<r:
            m=l+((r-l)//2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        rp = l
        if rp == 0:
            l, r = 0, len(nums) - 1
        elif target < nums[0]:
            l, r = rp, len(nums) - 1
        else:
            l, r = 0, rp - 1
        print(l,r)
        while l<=r:
            m=l+((r-l)//2)
            print(l,r,m, "vals: ", nums[m])
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return -1
        
        

            