class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(len(heights)):
            total = (n-i) * min(heights[i:n])
            res = max(total, res)
        return res