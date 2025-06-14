class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = list(sorted(set(nums)))
        return len(nums)

nums = [1,1,2,3,4]
nums = [2,10,10,30,30,30]


s = Solution()
x = s.removeDuplicates(nums)
print(x, nums)
