# url: https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self._min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            val = min(self.minStack[-1], val)
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minStack[-1]


class MinStackV2:

    def __init__(self):
        self.stack: list[tuple[int,int]]= []

    def push(self, val: int) -> None:
        m = min(self.stack[-1][1] if self.stack else val, val)
        self.stack.append((val,m))

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

s = MinStack()
s.push(1)
s.push(2)
s.push(0)
s.pop()

print(s.stack, s.getMin())

print(s.top())
