class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        while l<=r:
            m=l+(r-l)//2
            if matrix[m][0]<=target:
                l=m+1
            else:
                r=m-1
        row = matrix[l-1]
        l,r=0,len(row)
        while l<r:
            m=l+(r-l)//2
            if row[m]==target:
                return True
            if row[m]<target:
                l=m+1
            else:
                r=m
        return False