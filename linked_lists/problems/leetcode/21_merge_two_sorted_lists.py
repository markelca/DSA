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

class LinkedList:
    def __init__(self):
        self.sentinel = ListNode(-1)
        self.tail = self.sentinel

    def insertTailAll(self, vals):
        for val in vals:
            self.insertTail(val)

    def insertTail(self, val):
        new = ListNode(val)
        self.tail.next = new
        self.tail = new

    def print(self):
        cur = self.sentinel.next
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        print(vals)

    def removeAt(self, index):
        cur = self.sentinel
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next

    def insertAt(self, index, val):
        cur = self.sentinel
        i = 0
        while i < index and cur:
            i += 1
            cur = cur.next

        new = ListNode(val)
        if cur and cur.next:
            new.next = cur.next
            cur.next = new
        elif cur == self.tail:
            self.insertTail(val)


    def merge(self,ll):
        cur = self.sentinel.next
        i_cur = 0
        inserted = 0
        while cur:
            merging_cur = ll.sentinel.next
            i_merging_cur = 0
            while merging_cur:
                if merging_cur.val <= cur.val:
                    ll.removeAt(i_merging_cur)
                    self.insertAt(i_cur + inserted, merging_cur.val)
                    inserted += 1
                merging_cur = merging_cur.next
                i_merging_cur += 1

            cur = cur.next
            i_cur += 1


ll = LinkedList()
ll.insertTailAll([1,2,4])
ll2 = LinkedList()
ll2.insertTailAll([1,3,4])


ll.print()
# ll2.print()


ll.merge(ll2)

ll.print()
