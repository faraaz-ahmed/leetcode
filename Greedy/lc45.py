'''
45. Jump Game II
Medium
10.8K
377
Companies
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
Accepted
788.6K
Submissions
2M
Acceptance Rate
39.0%
'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        def getDestination(arr):
            if len(arr) < 1:
                return -1
            maxi, result = arr[0] + 0, 0
            for i in range(1, len(arr)):
                if arr[i] + i >= maxi:
                    maxi = arr[i] + i
                    result = i
            return result

        if len(nums) == 1:
            return 0
        i, count = 0, 0
        while i < len(nums) - 1:
            if nums[i] >= len(nums) - 1 - i:
                count += 1
                break
            destination = getDestination(
                nums[i: min(i + nums[i] + 1, len(nums))])
            if destination == -1 or (destination == 0 and (nums[i] + i) > len(nums) - 1):
                break
            elif (destination == 0 and (nums[i] + i) < len(nums) - 1):
                destination = nums[i]
            jumpTo = i + destination
            count += 1
            i = jumpTo
        return count
