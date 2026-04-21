class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            time = 0
            for i in range(len(piles)):
                eat = piles[i]
                while eat > 0:
                    eat -= k
                    time += 1
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res