from typing import Optional

class Node:
    def __init__(self, val: int, next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_val = self.next.val if self.next else None
        return f"Node(val={self.val}, next={next_val})"

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next  # type: ignore
        return cur.val  # type: ignore

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        # Removing head
        if index == 0:
            removed = self.head  # type: ignore
            self.head = removed.next  # type: ignore
            if self.size == 1:
                # list is now empty
                self.tail = None
            self.size -= 1
            return True

        # Find node *before* the one to remove
        prev = self.head  # type: ignore
        for _ in range(index - 1):
            prev = prev.next  # type: ignore

        removed = prev.next  # type: ignore
        prev.next = removed.next  # type: ignore
        if removed is self.tail:
            # removed the last element
            self.tail = prev

        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        values: list[int] = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values

    def printBounds(self) -> None:
        print("head:", self.head, "tail:", self.tail)

ll = LinkedList()
ll.insertTail(1)
ll.insertTail(2)
ll.insertTail(3)
ll.remove(0)
print(ll.getValues())  # [2, 3]
