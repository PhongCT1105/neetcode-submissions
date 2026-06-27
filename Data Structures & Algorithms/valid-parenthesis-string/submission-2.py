class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
            elif s[i] == ')':
                if left_stack:
                    left_stack.pop(-1)
                elif star_stack:
                    star_stack.pop(-1)
                else:
                    return False
            else:
                star_stack.append(i)
        
        while left_stack and star_stack:
            if left_stack[-1] < star_stack[-1]:
                star_stack.pop(-1)
                left_stack.pop(-1)
            else:
                return False

        return len(left_stack) <= 0
                