class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        maxLeft = 0
        maxRight = 0

        for i in range(len(height)):
            maxRight = max(height[i: len(height)])
            trapWater = min(maxLeft, maxRight) - height[i]
            maxLeft = max(maxLeft, height[i])
            if trapWater > 0:
                res += trapWater

        return res