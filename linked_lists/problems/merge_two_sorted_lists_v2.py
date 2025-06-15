# Definition for singly-linked list.
# url: https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"Node(val={self.val}, next={self.next.val if self.next else None})"

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1
        cur2 = list2
        result = LinkedList()

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                result.insertTail(cur1.val)
                cur1 = cur1.next
            else:
                result.insertTail(cur2.val)
                cur2 = cur2.next

        if cur1:
            result.appendTail(cur1)
        elif cur2:
            result.appendTail(cur2)

        return result.sentinel.next

class LinkedList:
    def appendTail(self, node):
        self.tail.next = node
        cur = node
        while cur:
            if not cur.next:
                break
            cur = cur.next
        self.tail = cur


    def __init__(self):
        self.sentinel = ListNode(-1)
        self.tail = self.sentinel

    def insertTail(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def print(self):
        cur = self.sentinel.next
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        print(values)

a = LinkedList()
a.insertTail(-9)
a.insertTail(3)
a.insertTail(5)
a.insertTail(12)

a.print()

b = LinkedList()
b.insertTail(5)
b.insertTail(7)

b.print()

s = Solution()
s.mergeTwoLists(a.sentinel.next,b.sentinel.next)
