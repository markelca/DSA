# url: https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        result = []
        for x in nums:
            if x != val:
                result.append(x)

        nums[:] = result
        return len(result)

nums = [1,1,2,3,4]
val = 1

s = Solution()

x = s.removeElement(nums,val)
print(x)
print(nums)


