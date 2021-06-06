class Solution(object):
  def maxSubArray(self, nums):
    curr_sum, max_sum = nums[0], nums[0]
    for i in range(1, len(nums)):
      curr_sum += nums[i]
      if nums[i] > max_sum and max_sum < 0:
        max_sum = nums[i]
        curr_sum = max_sum
      elif curr_sum > max_sum:
        max_sum = curr_sum
      elif curr_sum < 0:
        curr_sum = 0
    return max_sum
