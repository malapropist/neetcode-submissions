class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix)-1
        while l1 <= r1:
            m1 = (r1+l1)//2
            print(f"l:{l1}",f"r:{r1}",f"m:{m1}")
            print(matrix[m1])
            # whole array is less than target
            if matrix[m1][-1]<target:
                l1 = m1+1
            # whole array larger than target
            elif matrix[m1][0]>target:
                r1 = m1-1
            # array contains target
            elif matrix[m1][0]<=target and matrix[m1][-1]>=target:
                mat2 = matrix[m1]
                l2 = 0
                r2 = len(mat2)-1
                while l2<=r2:
                    m2 = (l2+r2)//2
                    if mat2[m2]<target:
                        l2 = m2+1
                    elif mat2[m2]>target:
                        r2 = m2-1
                    elif mat2[m2]==target:
                        return True
                return False
        return False