
from typing import Optional


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        q = Queue(students)

        prefs = {0:0,1:0}
        totalStudents = len(students)
        haveEaten = 0
        lastSw = 0

        i = 0
        rotations = 0
        while rotations < totalStudents:

            pref = q.consume()
            if pref is None:
                break


            prefs[pref] += 1



            sw = sandwiches[lastSw]

            if pref == sw:
                lastSw += 1
                haveEaten += 1
                prefs[pref] -= 1
                rotations = 0
            else:
                q.add(pref)
                rotations += 1




            if rotations == len(pref):  # no one can eat the current sandwich
                break

            if i > totalStudents and prefs[sw] == 0:
                break


        return totalStudents - haveEaten

class Queue:
    def __init__(self, arr):
        self.head = Student(-1)
        self.tail = self.head

        for p in arr:
            node = Student(p)
            self.tail.next = node
            self.tail = node

    def consume(self):
        h = self.head.next

        if self.head.next is None:
            return None
        self.head.next = h.next

        if self.head.next is None:
            self.tail = self.head

        return h.pref


    def add(self,pref):
        new = Student(pref)
        self.tail.next = new
        self.tail = new

    def print(self):
        cur = self.head.next
        while cur:
            print(cur.pref, end=' -> ')
            cur = cur.next
        print()

class Student:
    def __init__(self, pref):
        self.pref = pref
        self.next = None

    def __str__(self):
        return f"Student(pref={self.pref}, next={self.next.pref if self.next else None})"


# students = [1,1,0,0]
# sandwitches = [1,0,1,0]

students = [1,1,1,1]
sandwitches = [0,1,1,1]

students = [0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1]
sandwitches = [1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0]

s = Solution()

print(s.countStudents(students,sandwitches))

