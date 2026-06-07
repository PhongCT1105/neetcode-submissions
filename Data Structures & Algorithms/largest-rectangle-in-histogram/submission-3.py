class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force solution:
        # res = 0
        # i = 0
        # while i < len(heights):
        #     l, r = i, i
        #     while l >= 0 and heights[l] >= heights[i]:
        #         l -= 1
        #     while r < len(heights) and heights[r] >= heights[i]:
        #         r += 1
            
        #     area = heights[i] * (r - l - 1)
        #     res = max(res, area)
        #     i += 1

        # return res

        # Optimal monotonic stack solution: O(N)
        res = 0
        stack = []

        for i in range(len(heights)):
            # Cannot expand
            start = i
            while stack and heights[i] < stack[-1][1]:
                num = stack.pop()
                area = num[1] * (i - num[0])
                res = max(res, area)
                start = num[0]
            
            stack.append((start, heights[i]))

        for i in range(len(stack)):
            area = stack[i][1] * (len(heights) - i)
            res = max(area, res)

        return res