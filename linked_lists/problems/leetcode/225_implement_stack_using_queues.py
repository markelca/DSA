from collections import deque



class MyStack(object):

    def __init__(self):
        self.q1 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)


    def pop(self):
        """
        :rtype: int
        """
        res = None

        i = 0
        while self.q1:
            res = self.q1.popleft()
            if i < len(self.q1):
                self.q1.append(res)
            else:
                break
            i += 1

        return res

    def top(self):
        """
        :rtype: int
        """
        return self.q1[len(self.q1)-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1

s = MyStack()
s.push(1)

print(s.pop())

print(s.q1)

print(s.empty())
