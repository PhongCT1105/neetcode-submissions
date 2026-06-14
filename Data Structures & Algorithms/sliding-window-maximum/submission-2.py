class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # # Brute force
        # res = []
        # l, r = 0, k-1
        # while r < len(nums):
        #     res.append(max(nums[l:r+1]))
        #     l += 1
        #     r += 1
        # return res

        # Monotonic stack
        from collections import deque
        stack = deque([])
        res = []
        i = 0
        
        while i < len(nums):
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            stack.append((nums[i],i))
            # Remove the expire
            while stack and stack[0][1]+k-1 < i:
                stack.popleft()
            # Return if i >= k:
            if i >= k-1: 
                res.append(stack[0][0])
            i += 1
        return res
