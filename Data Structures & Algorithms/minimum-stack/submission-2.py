import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum) == 0:
            self.minimum.append(val)
        else:
            print(self.minimum)
            if self.minimum[len(self.minimum) - 1] > val:
                self.minimum.append(val)
            else:
                self.minimum.append(self.minimum[len(self.minimum) - 1])

    def pop(self) -> None:
        num = self.stack.pop()
        low = self.minimum.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minimum[len(self.minimum) - 1]
