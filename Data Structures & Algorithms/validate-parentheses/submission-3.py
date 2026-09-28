class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        cls_bracket = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        for c in s:
            if c in open_bracket:
                stack.append(c)
            else:
                if not stack:
                    return False
                if cls_bracket[c] != stack[-1]:
                    return False
                else:
                    stack.pop(-1)
        
        if stack:
            return False
        else:
            return True
                