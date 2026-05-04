class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        r = x
        res = 0

        while l <= r:
            mid = (l + r) // 2
            sqrt = mid * mid  
            if sqrt > x:
                r = mid - 1
            elif sqrt < x:
                res = mid
                l = mid + 1
            else:
                return mid

        return res