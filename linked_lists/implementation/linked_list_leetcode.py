class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node(val={self.val}, next={self.next.val if self.next else None})"

class MyLinkedList(object):

    def __init__(self):
        self._head = Node(-1)
        self._tail = self._head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self._head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new = Node(val,self._head.next)
        self._head.next = new

        if self._head == self._tail:
            self._tail = new


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new = Node(val)
        self._tail.next = new
        self._tail = new

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self._head
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1

        new = Node(val)

        if cur and cur.next:
            new.next = cur.next
            cur.next = new
        elif cur:
            self._tail = new
            cur.next = new


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        cur = self._head
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1

        if cur and cur.next:
            if cur.next == self._tail:
                self._tail = cur
            cur.next = cur.next.next

    def print(self):
        cur = self._head.next
        while cur:
            print(cur.val, "->", end=' ')
            cur = cur.next
        print()

# Your MyLinkedList object will be instantiated and called as such:
ll = MyLinkedList()
# param_1 = ll.get(0)
ll.addAtHead(1)
ll.addAtHead(2)
ll.addAtHead(3)
ll.addAtTail(11)
ll.addAtTail(22)


print(ll._tail)
ll.addAtIndex(5,88)
print(ll._tail)


ll.print()
ll.deleteAtIndex(5)
ll.print()
print(ll._head.next)

print('------------')
ll = MyLinkedList()
ll.deleteAtIndex(0)
ll.addAtTail(4)
ll.addAtTail(5)
ll.addAtTail(6)
ll.print()
ll.addAtIndex(2,33)
ll.print()
print(ll._tail)

# print(ll.get(0))


# print(ll._tail.val)
# print(ll._head.next.val)
