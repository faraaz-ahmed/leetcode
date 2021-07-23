class Solution:
  def partitionDisjoint(self, nums: List[int]) -> int:
    max_, maxSoFar, index = nums[0], nums[0], 0
    for i in range(1, len(nums)):
      if maxSoFar > nums[i]:
        index = i
        maxSoFar = max_
      else:
        max_ = max(max_, nums[i])
    return index + 1