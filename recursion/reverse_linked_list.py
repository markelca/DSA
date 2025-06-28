# Definition for singly-linked list.
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional[ListNode]=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head

        if head.next.next is None:
            n = ListNode(head.next.val)
            n.next = head
            head.next = None
            return n

        n = self.reverseList(head.next)
        tmp = head.next
        head.next = None
        tmp.next = head
        return n


cur = Solution().reverseList(ListNode(1))
# cur = Solution().reverseList(ListNode(0,ListNode(1,ListNode(2,ListNode(3)))))
while cur:
    print(cur.val, end='->')
    cur = cur.next
