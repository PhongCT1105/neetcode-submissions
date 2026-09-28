class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        notation = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in notation:
                right = stack.pop()
                left = stack.pop()
                if token == '*':
                    stack.append(left*right)
                elif token == '/':
                    stack.append(int(left/right))
                elif token == '+':
                    stack.append(left+right)
                elif token == '-':
                    stack.append(left-right)
            else:
                stack.append(int(token))
        
        return int(stack[-1])