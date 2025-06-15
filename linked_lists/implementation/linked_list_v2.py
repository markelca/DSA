# url: https://neetcode.io/problems/singlyLinkedList
# This approaches uses a dummy (or sentinel) element as the head, which simplifies the implementation

from typing import Optional


class LinkedList:
    def __init__(self):
        self.head: Node = Node(-1)
        self.tail: Node = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val, self.head.next)
        if not new.next:
            self.tail = new

        self.head.next = new


    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0

        while i < index and cur:
            cur = cur.next
            i += 1
                    
        if not (cur and cur.next):
            return False

        if cur.next == self.tail:
            self.tail = cur

        cur.next = cur.next.next
        return True


    def getValues(self) -> list[int]:
        vals = []
        cur = self.head.next
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals

class Node:
    def __init__(self, val: int, next: Optional['Node'] = None):
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
