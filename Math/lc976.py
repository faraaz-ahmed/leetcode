# #976. Largest Perimeter Triangle
# Easy
# 1.9K
# 257
# Companies
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
#
#
#
# Example 1:
#
# Input: nums = [2,1,2]
# Output: 5
# Example 2:
#
# Input: nums = [1,2,1]
# Output: 0
#
#
# Constraints:
#
# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106
# Accepted
# 137.4K
# Submissions
# 255K
# Acceptance Rate
# 53.9%

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
            nums.pop(0)
        return sum(nums[:3]) if len(nums) > 2 else 0