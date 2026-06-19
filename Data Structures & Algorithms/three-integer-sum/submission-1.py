class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        ans=[]
        for i,val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return ans
