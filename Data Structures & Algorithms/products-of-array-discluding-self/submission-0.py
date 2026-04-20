class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1], []
        total = 1
        for num in nums:
            total *= num
            prefix.append(total)
        prefix.pop(-1)

        for i in range(len(nums)-1, -1, -1):
            total *= num[i]
            postfix.append(total)
        postfix.pop(0)
        postfix.append(1)
        res = []

        for i in range(len(nums)):
            total = prefix[i] * postfix[i]
            res.append(total)
        return res