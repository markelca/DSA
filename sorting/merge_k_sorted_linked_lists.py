from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next.val if self.next else None})"

    def print(self):
        cur = self
        while cur:
            print(cur.val, end=' -> ')
            cur = cur.next
        print()


def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r):
        if l > r:
            return None

        if l == r:
            return lists[l]

        m = (l + r) // 2

        left = self.divide(lists,l,m)
        right = self.divide(lists, m+1,r)

        return self.merge(left, right)



    def merge(self, l: Optional[ListNode], r: Optional[ListNode]):
        dummy = ListNode(-1)
        cur = dummy

        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next

            cur = cur.next

        if l:
            cur.next = l
        if r:
            cur.next = r

        return dummy.next

lists_input = [
    [1, 2, 4],
    [1, 3, 5],
    [3, 6],
]
arr = [build_linked_list(vals) for vals in lists_input]

l = Solution().mergeKLists(arr)
if l:
    l.print()
else:
    print('solution empty')
