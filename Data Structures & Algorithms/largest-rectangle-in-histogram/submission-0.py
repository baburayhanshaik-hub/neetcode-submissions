class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        stack = []
        for i,j in enumerate(heights):
            start = i
            while stack and j<stack[-1][0]:
                h,ind = stack.pop()
                w = i-ind
                a = w*h
                area = max(a,area)
                start = ind
            stack.append((j,start))
        while stack:
            h,ind = stack.pop()
            w = n-ind
            area = max(area, w*h)
        return area