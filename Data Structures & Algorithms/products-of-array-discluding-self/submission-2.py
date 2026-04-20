class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1], []
        total = 1
        for num in nums:
            total *= num
            prefix.append(total)
        print(prefix)
        prefix.pop(-1)

        total = 1
        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            postfix.append(total)

        postfix.pop(-1)
        postfix.insert(0, 1)
        res = []
        print(prefix, postfix)
        for i in range(len(nums)):
            total = prefix[i] * postfix[len(nums)-1-i]
            res.append(total)
        return res