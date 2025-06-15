class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.dummy = Node(-1)  # sentinel head
        self.tail = self.dummy
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        new = Node(val, prev=self.dummy, next=self.dummy.next)
        if self.dummy.next:
            self.dummy.next.prev = new
        self.dummy.next = new
        if self.tail is self.dummy:
            self.tail = new
        self.size += 1

    def addAtTail(self, val):
        new = Node(val, prev=self.tail, next=None)
        self.tail.next = new
        self.tail = new
        if self.dummy.next is None:
            self.dummy.next = new
        self.size += 1

    def addAtIndex(self, index, val):
        # optionally clamp negative to zero
        if index < 0:
            index = 0
        if index > self.size:
            return

        # find the node currently at `index` (or None if appending)
        cur = self.dummy
        for _ in range(index):
            cur = cur.next

        # insert after `cur`
        new = Node(val, prev=cur, next=cur.next)
        if cur.next:
            cur.next.prev = new
        cur.next = new

        # if appending at tail, update tail pointer
        if new.next is None:
            self.tail = new

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        # find the node to delete
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next

        # unlink it
        prev_node = cur.prev
        next_node = cur.next
        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        else:
            # deleting the tail
            self.tail = prev_node

        self.size -= 1
