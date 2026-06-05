class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        for i in range(len(height)):
            maxLeft = max(height[0:i+1])
            maxRight = max(height[i: len(height)])
            trapWater = min(maxLeft, maxRight) - height[i]
            if trapWater > 0:
                res += trapWater

        return res