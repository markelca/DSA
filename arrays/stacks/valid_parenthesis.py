# url: https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        closer_map = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        closers = closer_map.keys()
        for c in s:
            if c in closers:
                if len(stack) == 0:
                    return False

                if stack[-1] == closer_map[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return len(stack) == 0


s = "([]))"
s = "()[]{}"
s = "([])"
s = "(]"
s = "(])"
s = "[)(]"
print(Solution().isValid(s))
