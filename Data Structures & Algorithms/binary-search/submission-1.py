class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid]<target:
                print("left", "val:"+str(nums[mid]), "l:"+str(l), "r:"+str(r), "m:"+str(mid))
                l = mid+1
            elif nums[mid]>target:
                print("right", "val:"+str(nums[mid]), "l:"+str(l), "r:"+str(r), "m:"+str(mid))
                r = mid-1
            else:
                print("mid", "val:"+str(nums[mid]), "l:"+str(l), "r:"+str(r), "m:"+str(mid))

                return mid
        print("end", "val:"+str(nums[mid]), "l:"+str(l), "r:"+str(r), "m:"+str(mid))
        
        return -1