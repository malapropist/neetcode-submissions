class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,2,7] [3,4,5,6]
        # total_len = len(nums)+len(nums2)
        # n2_len = total_len
        # l = 0
        # r = len(nums1)-1
        # while l<=r:
        #     mid = (l+r)//2
        #     opp = len(nums2)-mid
        #     if nums1[mid] > nums2[opp+1]:
        #         r = mid-1
        #     elif nums2[opp] > nums1[mid+1]
        #         l = mid+1
        nums1=nums1+nums2
        nums1.sort()
        med = (len(nums1)-1)/2
        print("med: ", med)
        print(nums1)
        if med%1 == 0.5:
            return (nums1[int(med)]+nums1[int(med+1)])/2
        else:
            return nums1[int(med)]