# class Solution:
#     def getIndex(self, i, j):
#         return str(i) + '+' + str(j)
#
#     def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
#         # dp = [[] * j]
#         # dp[0].append(nums[0])
#         dp = {}
#         # dp[self.getIndex(0, 0)] = nums[0]
#         count = 0
#         for i in range(0, len(nums)):
#             for j in range(i, len(nums)):
#                 # print(i, j, nums[j], dp, self.getIndex(i, j), self.getIndex(i, j) in dp)
#                 if not self.getIndex(i, j) in dp:
#                     # print(i, j, nums[j])
#                     if j == i:
#                         dp[self.getIndex(i, j)] = nums[i]
#                         # print(i, j, nums[j], dp[self.getIndex(i, j - 1)])
#                         count += 1 if nums[i] >= left and nums[i] <= right else 0
#                     elif j - 1 >= 0 and j - 1 < len(nums) and self.getIndex(i, j - 1) in dp:
#                         # print(i, j, nums[j], dp[self.getIndex(i, j - 1)])
#                         dp[self.getIndex(i, j)] = max(dp[self.getIndex(i, j - 1)], nums[j])
#                         if (dp[self.getIndex(i, j)] >= left and dp[self.getIndex(i, j)] <= right):
#                             count += 1
#                     # elif j + 1 >= 0 and j + 1 < len(nums)self.getIndex(i, j + 1) in dp:
#                     #     dp[self.getIndex(i, j)] = max(dp[self.getIndex(i, j - 1)], nums[j])
#                     #     if (dp[self.getIndex(i, j)] >= left and dp[self.getIndex(i, j)] <= right):
#                     #         count += 1
#         # print(dp)
#
#         return count


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, low, mid = 0, 0, 0
        for num in nums:
            if num > right: mid = 0
            else:
                mid += 1
                ans += mid
            if num >= left: low = 0
            else:
                low += 1
                ans -= low
        return ans