class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minVal:
            self.minVal = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minVal and len(self.stack) > 0:
            low = self.stack[0]
            for num in self.stack:
                if num < low:
                    low = num
            self.minVal = low
        elif len(self.stack) == 0:
            self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
