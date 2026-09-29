class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h >= piles length => max speed = max(piles) => finish in length hour

        l, r = 1, max(piles)
        res = r 

        while l <= r:
            speed = (l+r) // 2
            # Check if speed is sastify
            time = 0
            for pile in piles:
                if pile%speed == 0:
                    time += (pile//speed)
                else:
                    time += (pile//speed)+1
            if time > h: #Slow
                l = speed + 1
            else: #Sastify finding a lower speed
                res = min(res, speed)
                r = speed - 1 

        return res