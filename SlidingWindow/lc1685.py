# 1685. Sum of Absolute Differences in a Sorted Array
# Medium
# 1.9K
# 66
# Companies
# You are given an integer array nums sorted in non-decreasing order.

# Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

# Example 1:

# Input: nums = [2,3,5]
# Output: [4,3,5]
# Explanation: Assuming the arrays are 0-indexed, then
# result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
# result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
# result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
# Example 2:

# Input: nums = [1,4,6,8,10]
# Output: [24,15,13,15,21]
 

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i] <= nums[i + 1] <= 104
# Accepted
# 96.2K
# Submissions
# 138.7K
# Acceptance Rate
# 69.4%

class Solution:
  def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    # sum(abs(nums[i] - nums[j])) for all len(nums)>j>=0
    # abs(nums[i] - nums[j]) + abs(nums[i] - nums[j + 1]) +.....+ abs(nums[i] - nums[n])
    result, sum_right, sum_left = [], 0, 0
    for num in nums:
      sum_right += num
    n = len(nums)
    for i in range(0, n):
      result.append((i) * nums[i] - sum_left - ((n - i) * nums[i] -  sum_right))
      sum_left += nums[i]
      sum_right -= nums[i]
    return result