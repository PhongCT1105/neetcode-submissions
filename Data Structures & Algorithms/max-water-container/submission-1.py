class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def getArea(l, r):
            return min(heights[l], heights[r]) * (r-l)
        n = len(heights)
        l, r = 0, n-1
        res = 0
        while l < r:
            res = max(res, getArea(l,r))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res