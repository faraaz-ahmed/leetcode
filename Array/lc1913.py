class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) - 2] * nums[len(nums) - 1] - nums[0] * nums[1]
