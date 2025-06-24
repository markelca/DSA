from collections import deque


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students = deque(students)

        count = 0
        while students and count < len(students):
            st = students.popleft()
            if st == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(st)
                count += 1

        return len(students)

# students = [1,1,0,0]
# sandwitches = [1,0,1,0]

# students = [1,1,1,0]
# sandwitches = [0,1,1,1]

students = [0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1]
sandwitches = [1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0]

s = Solution()

print(s.countStudents(students,sandwitches))

