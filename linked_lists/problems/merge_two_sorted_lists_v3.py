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
        sentinel = ListNode()
        tail = sentinel

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return sentinel.next

l1 = ListNode(1,ListNode(2,ListNode(4)))
l2 = ListNode(1,ListNode(3,ListNode(4)))

s = Solution().mergeTwoLists(l1,l2)
while s:
    print(s.val, ',', end=' ')
    s = s.next
