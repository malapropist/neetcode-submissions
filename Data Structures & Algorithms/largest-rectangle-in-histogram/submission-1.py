class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s=[] # (idx, height)
        max_area=0

        for i,h in enumerate(heights):
            start = i
            while len(s) and s[-1][1]>h:
                idx, height = s.pop()
                max_area = max((i-idx)*height,max_area)
                start = idx
            s.append((start,h)) 
        
        while len(s):
            idx, hei = s.pop()
            max_area = max((len(heights)-idx)*hei,max_area)
        return max_area