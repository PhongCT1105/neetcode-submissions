class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre, post = [], []
        # Calculate prefix
        num = 1
        for i in range(0,len(nums)):
            pre.append(num*nums[i])
            num *= nums[i]
        pre.insert(0, 1)
        pre.pop()
        # Calculate postfix
        num = 1
        for i in range(len(nums)-1, -1, -1):
            post.append(num*nums[i])
            num *= nums[i]
        post.pop()
        post.insert(0, 1)
        res = []
        for i in range(len(nums)):
            res.append(pre[i]*post[len(nums)-1-i])

        return res