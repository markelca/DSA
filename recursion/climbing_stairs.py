# class Solution:
#     def climbStairs(self, n: int) -> int:
#         
#         def dfs(i):
#             if i >= n:
#                 return i == n
#             return dfs(i + 1) + dfs(i + 2)
#             
#         return dfs(0)



class SolutionV2:
    def climbStairs(self, n: int) -> int:
        a, b, c = 0, 1, 0
        
        for _ in range(n):
            c = a + b
            a, b = b, c
        
        return b

# print(Solution().climbStairs(38))

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # We'll use two variables to keep track of the number of ways to
        # reach the two preceding steps.
        # Let's initialize them for the results of n=1 and n=2.
        two_steps_before = 1  # Represents ways(i-2)
        one_step_before = 2  # Represents ways(i-1)

        # We can now loop from step 3 up to n to find the final answer.
        for _ in range(3, n + 1):
            # The number of ways to reach the current step 'i' is the sum
            # of the ways to reach the previous two steps.
            current_ways = one_step_before + two_steps_before

            # Now, we update our variables for the next loop iteration.
            # The step that was one step before is now two steps before.
            two_steps_before = one_step_before
            # The current number of ways becomes the new "one step before".
            one_step_before = current_ways

        # After the loop, 'one_step_before' holds the total ways for 'n' steps.
        return one_step_before


# --- Example Usage ---
solver = Solution()

# For n = 2
print(f"Ways to climb 2 stairs: {solver.climbStairs(2)}")  # Output: 2

# For n = 3
print(f"Ways to climb 3 stairs: {solver.climbStairs(3)}")  # Output: 3

# For n = 5
print(f"Ways to climb 5 stairs: {solver.climbStairs(5)}")  # Output: 8 assert Solution().climbStairs(38) == 63245986

print(Solution().climbStairs(38))
