class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        maxLeft = 0
        maxRight = 0
        maxRight_id = []

        for i in range(len(height)-1, -1, -1):
            maxRight = max(maxRight, height[i])
            maxRight_id.append(maxRight)

        for i in range(len(height)):

            maxRight = maxRight_id[len(maxRight_id)-1-i]
            trapWater = min(maxLeft, maxRight) - height[i]
            maxLeft = max(maxLeft, height[i])
            if trapWater > 0:
                res += trapWater

        return res