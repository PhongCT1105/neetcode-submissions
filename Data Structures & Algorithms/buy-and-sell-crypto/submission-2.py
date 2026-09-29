class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 0

        # Algorithm:
        # Day smaller than current l, update l because better price
        # Day larger than current l, update res and extend the right window
        res = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return res    
