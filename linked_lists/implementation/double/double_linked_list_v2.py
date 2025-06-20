from __future__ import annotations
from typing import Optional



class Node:
    def __init__(self, val, prev: Optional[Node] = None, next: Optional[Node] = None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"Node(prev={self.prev.val if self.prev else None}, val={self.val}, next={self.next.val if self.next else None})"

class MyLinkedList(object):
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        cur = self.head.next
        while index > 0 and cur and cur != self.tail:
            cur = cur.next
            index -= 1
        return cur.val if cur and cur != self.tail and index == 0 else -1


    def addAtHead(self, val):
        new = Node(val, prev=self.head, next=self.head.next)
        self.head.next.prev = new
        self.head.next = new


    def addAtTail(self, val):
        new = Node(val,prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = new
        self.tail.prev = new

    def addAtIndex(self, index, val):
        cur = self.head.next
        while index > 0 and cur and cur != self.tail:
            index -= 1
            cur = cur.next

        if index > 0:
            return

        new = Node(val)
        new.prev = cur.prev
        new.next = cur

        cur.prev.next = new
        cur.prev = new

    def deleteAtIndex(self, index):
        cur = self.head.next
        while index > 0 and cur and cur != self.tail:
            cur = cur.next
            index -= 1

        if index > 0 or cur == self.tail:
            return

        cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def printValues(self):
        cur = self.head.next
        values = []
        while cur and cur != self.tail:
            values.append(cur.val)
            cur = cur.next
        print(values)

    def print(self):
        cur = self.head.next
        while cur and cur != self.tail:
            print(cur, end=' -> ')
            cur = cur.next
        print()

    def printBounds(self):
        print("Head:", self.head.next)
        print("Tail:", self.tail.prev)

ll = MyLinkedList()
ll.addAtTail(1)
ll.addAtTail(2)
ll.addAtTail(3)
ll.addAtHead(1)
ll.addAtHead(2)
ll.addAtHead(3)

ll.addAtIndex(7,77)

ll.deleteAtIndex(6)

print('-------')
ll.printValues()
ll.print()
ll.printBounds()

