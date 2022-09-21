# class Solution:
#     def bruteForce(self, nums: List[int], multipliers: List[int]) -> int:
#         dp = {}
#         length = len(nums)
#         dp['0,' + length] = 0
#         dp['0,' + length - 1] = nums[length - 1]
#         dp['1,' + length - 1] = nums[0]
#         dp[]
#         def bruteForceImpl(n, m, prod, i, start, end):
#             if start >= end or i == len(m):
#                 return max(n[start] * prod, n[end] * prod)
#             else:
#                 return max(bruteForceImpl(n[start + 1:], m, prod * n[start], i + 1, start + 1, end), bruteForceImpl(n[:end - 1], m, prod * n[end], i + 1, start, end - 1))

class Solution:
  def printState(self, start, end, op):
    print('start =', start, 'end = ',end, 'op = ', op)
  def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    memo = {}
    m = len(multipliers)
    n = len(nums)
    def dp(start, end, op):
      if op == m:
        return 0
      if (start, end, op) in memo:
        return memo[(start, end, op)]
      left = nums[start] * multipliers[op] + dp(start + 1, end, op + 1)
      # self.printState(start, end, op)
      right = nums[end] * multipliers[op] + dp(start, end - 1, op + 1)
      # self.printState(start, end, op)
      # print('****', '****', left, right)
      memo[(start, end, op)] = max(left, right)
      return memo[(start, end, op)]
    # dp(0, n - 1, 0)
    # print(memo, nums[1], multipliers[1], m)
    return dp(0, n - 1, 0)
    # def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    #     states = []
    #     return 0


class Solution:
  def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    memo = {}
    m = len(multipliers)
    n = len(nums)
    def dp(start, end, op):
      if op == m:
        return 0
      if (start, end, op) in memo:
        return memo[(start, end, op)]
      left = nums[start] * multipliers[op] + dp(start + 1, end, op + 1)
      right = nums[end] * multipliers[op] + dp(start, end - 1, op + 1)
      memo[(start, end, op)] = max(left, right)
      return memo[(start, end, op)]
    return dp(0, n - 1, 0)


class Solution:
  def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    memo = {}
    m = len(multipliers)
    n = len(nums)
    # op = n - (end + 1 - start)
    #end = n - 1 + start - op
    def dp(start,op):
      if op == m:
        return 0
      if (start, op) in memo:
        return memo[(start, op)]
      left = nums[start] * multipliers[op] + dp(start + 1, op + 1)
      right = nums[n - 1 + start - op] * multipliers[op] + dp(start, op + 1)
      memo[(start, op)] = max(left, right)
      return memo[(start, op)]
    return dp(0, 0)
# 1770. Maximum Score from Performing Multiplication Operations
# Medium

# 1342

# 331

# Add to List

# Share
# You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Remove x from the array nums.
# Return the maximum score after performing m operations.

 

# Example 1:

# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
# Example 2:

# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

# Constraints:

# n == nums.length
# m == multipliers.length
# 1 <= m <= 103
# m <= n <= 105
# -1000 <= nums[i], multipliers[i] <= 1000



