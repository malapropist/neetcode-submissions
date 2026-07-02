class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)
        while l<r:
            m = (l+r)//2
            if matrix[m][0]<=target:
                l = m+1
            else:
                r = m
        n = matrix[l-1]
        print(n)
        l,r=0,len(n)-1
        while l<=r:
            m = (l+r)//2
            if n[m]==target:
                return True
            elif n[m]>target:
                r=m-1
            else:
                l=m+1
        return False