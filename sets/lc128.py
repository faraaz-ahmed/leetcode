class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_ = 0
        for x in nums:
            if x - 1 not in numset:
                y = x + 1
                while y in numset:
                    y += 1
                max_ = max(y - x, max_)
        return max_
