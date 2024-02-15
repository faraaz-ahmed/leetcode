# 1814. Count Nice Pairs in an Array
# Medium
# 1.6K
# 66
# Companies
# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
# Example 2:

# Input: nums = [13,10,35,24,76]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109

class Solution:
  def countNicePairs(self, nums: List[int]) -> int:
    map_ = {}
    for num in nums:
      rev = num - int(str(num)[::-1])
      if rev in map_:
        map_[rev] += 1
      else:
        map_[rev] = 1
    sum_ = 0
    for key in map_.keys():
      sum_ += (map_[key] * (map_[key] - 1)) // 2 if map_[key] >= 2 else 0
    return sum_ % (10 ** 9 + 7)