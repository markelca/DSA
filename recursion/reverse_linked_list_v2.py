class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

# cur = Solution().reverseList(ListNode(1))
cur = Solution().reverseList(ListNode(0,ListNode(1,ListNode(2,ListNode(3)))))
while cur:
    print(cur.val, end='->')
    cur = cur.next
