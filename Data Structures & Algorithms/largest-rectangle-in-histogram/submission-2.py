class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        while i < len(heights):
            l, r = i, i
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            while r < len(heights) and heights[r] >= heights[i]:
                r += 1
            
            area = heights[i] * (r - l - 1)
            res = max(res, area)
            i += 1

        return res