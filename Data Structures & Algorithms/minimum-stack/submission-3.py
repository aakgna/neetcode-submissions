import heapq
class MinStack:

    def __init__(self):
        self.actual = list()
        self.mini = list()

    def push(self, val: int) -> None:
        self.actual.append(val)
        if self.mini:
            self.mini.append(min(val, self.mini[-1]))
        else:
            self.mini.append(val)

    def pop(self) -> None:
        self.mini.pop()
        return self.actual.pop()

    def top(self) -> int:
        return self.actual[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
