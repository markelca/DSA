# url: https://neetcode.io/problems/concatenation-of-array
class SolutionV2:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums * 2

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        new = nums.copy()
        for x in nums:
            new.append(x)
        return new

nums = [1,4,1,2]
print(Solution().getConcatenation(nums))
