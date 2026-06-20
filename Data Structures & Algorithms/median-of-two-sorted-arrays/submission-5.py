class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<len(nums2):
            A,B=nums1,nums2
        else:
            A,B=nums2,nums1
        t_length = len(nums1)+len(nums2)
        half=t_length//2
        l,r=0,len(A)-1
        while 1:#l<=r:
            m1=(l+r)//2
            m2 = half-m1-2
            print(l,r, m1,m2)
            #border values to splits
            Aleft=A[m1] if m1>=0 else float("-inf")
            Aright=A[m1+1] if (m1+1)<len(A) else float("inf")
            
            Bleft=B[m2] if m2>=0 else float("-inf")
            Bright=B[m2+1] if (m2+1)<len(B) else float("inf")
            # verify split location
            if Aleft<=Bright and Bleft<=Aright:
                if t_length%2==1:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=m1-1
            else:
                l=m1+1
