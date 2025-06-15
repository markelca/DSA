# url: https://neetcode.io/problems/singlyLinkedList
from __future__ import annotations
from typing import Optional

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val, self.head)
        if not self.head:
            self.tail = new

        self.head = new

    def insertTail(self, val: int) -> None:
        new = Node(val)
        if not self.tail:
            self.head = new
        else:
            self.tail.next = new

        self.tail = new


    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0

        if index == 0 and self.head:
            self.head = self.head.next if self.head else None
            return True

        while cur:
            if i + 1 == index:
                if not cur.next:
                    return False

                if cur.next == self.tail:
                    self.tail = cur

                cur.next = cur.next.next if cur.next else None
                return True
            cur = cur.next
            i += 1

        return False

    def getValues(self) -> list[int]:
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals

class Node:
    def __init__(self, val: int, next: Optional[Node] = None):
        self.val = val
        self.next = next
        pass

    def __str__(self) -> str:
        return f"Node(val={self.val}, next={self.next})"

ll = LinkedList()
ll.insertHead(1)
ll.insertHead(2)
ll.insertHead(3)

print(ll.getValues())

print(ll.head)
ll.remove(0)
print(ll.head)
ll.remove(1)

print(ll.getValues())
