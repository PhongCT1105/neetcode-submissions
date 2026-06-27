class Solution:
    def checkValidString(self, s: str) -> bool:
        free = 0
        stack = []

        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                if stack:
                    stack.pop(-1)
                elif free > 0:
                    free -= 1
                else:
                    return False
            else:
                free += 1

        while free>0 and stack:
            stack.pop(-1)
            free -= 1
        
        return len(stack) <= 0
                