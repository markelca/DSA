from collections import deque
from typing import Any, List



class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1


    def pop(self):
        """
        :rtype: int
        """
        return self.q1.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) > 0 

s = MyStack()
s.push(1)
s.push(2)

print(s.q1)
print(s.q2)

print(s.pop())
# print(s.top())
# print(s.empty())
