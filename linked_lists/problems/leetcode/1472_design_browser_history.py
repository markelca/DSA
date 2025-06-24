from typing import Optional


class Page:
    next: Optional['Page']
    prev: Optional['Page']

    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f"Page(prev={self.prev.val if self.prev else None}, val={self.val}, next={self.next.val if self.next else None})"

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = Page("<dummy>")
        self.tail = Page("<dummy>")
        self.head.next = self.tail
        self.tail.prev = self.head

        new = Page(homepage)
        new.prev = self.head
        new.next = self.tail
        self.head.next = new
        self.tail.prev = new

        self.cur = new

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new = Page(url)
        new.next = self.tail
        new.prev = self.cur

        self.cur.next = new
        self.tail.prev = new

        self.cur = new

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        cur = self.cur
        while steps > 0 and cur and cur.prev != self.head:
            steps -= 1
            cur = cur.prev

        self.cur = cur
        return cur.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        cur = self.cur
        while steps > 0 and cur and cur.next != self.tail:
            cur = cur.next
            print(cur)
            steps -= 1

        self.cur = cur
        return cur.val

    def print(self):
        cur = self.head.next
        while cur and cur != self.tail:
            if cur == self.cur:
                print(f"({cur.val})", end=" -> ")
            else:
                print(cur.val, end=" -> ")
            cur = cur.next
        print()


homepage = "leetcode.com"
h = BrowserHistory(homepage)
h.visit("google.com")
h.visit("facebook.com")
h.visit("youtube.com")
print(h.back(1))
print(h.back(1))
print(h.forward(1))
h.visit("linkedin.com")
print(h.forward(2))
print(h.back(2))
print(h.back(7))
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
