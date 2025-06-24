# Definition for singly-linked list.
# url: https://leetcode.com/problems/reverse-linked-list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        ll = LinkedList()
        while cur:
            ll.insertHead(cur.val)
            cur = cur.next

        return ll.getHead()


class LinkedList:
    def __init__(self):
        self._head = ListNode(-1)
        self.tail = self._head

    def insertHead(self, val):
        new = ListNode(val, self._head.next)
        self._head.next = new
        if not new.next:
            self.tail = new

    def getHead(self):
        return self._head.next

    def print(self):
        cur = self._head.next
        while cur:
            print(cur.val, "->", end=" ")
            cur = cur.next

ll = LinkedList()
ll.insertHead(1)
ll.insertHead(2)
ll.insertHead(3)
ll.insertHead(4)
ll.insertHead(5)


ll.print()
