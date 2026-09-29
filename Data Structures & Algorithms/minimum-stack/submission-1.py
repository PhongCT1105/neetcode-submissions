class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.minVal, val)
        self.minStack.append(self.minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.minVal = self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
