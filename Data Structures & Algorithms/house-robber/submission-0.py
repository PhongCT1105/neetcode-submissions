class Solution:
    def rob(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)
        def backtrack(i, total):
            if i >= n:
                nonlocal res
                res = max(res,total)
                return

            total += nums[i]
            backtrack(i+2, total)
            total -= nums[i]
            backtrack(i+1, total)
        backtrack(0, 0)
        return res