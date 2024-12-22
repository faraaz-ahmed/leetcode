class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if (nums[abs(nums[i]) - 1] < 0):
                return abs(nums[i])
            nums[abs(nums[i]) - 1] = (-1) * nums[abs(nums[i]) - 1]
        return 0