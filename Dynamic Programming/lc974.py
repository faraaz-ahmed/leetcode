"""974. Subarray Sums Divisible by K
Medium
5.4K
217
Companies
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * len(nums)
        sum_ = 0
        for i in range(0, len(nums)):
            sum_ += nums[i]
            prefixSum[i] = sum_
        freqMemo = {}
        freqMemo[0] = 1
        count = 0
        temp = []
        print(prefixSum)
        for i in range(0, len(nums)):
            remainder = prefixSum[i] % k
            temp.append(remainder)
            if remainder in freqMemo:
                count += freqMemo[remainder]
                freqMemo[remainder] += 1
            else:
                if remainder == 0:
                    count += 1
                freqMemo[remainder] = 1
        print(temp)
        return count


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # frequency table to store the frequency of the remainder
        remainderFrq = defaultdict(int)
        # Empty sub array will have a sum of 0 and remainder of 0, thus the frequency of 0 is 1 before we go into the array
        remainderFrq[0] = 1

        res = prefixSum = 0
        for n in nums:
            # Adding n to the prefixSum, so we have the prefixSum up to the ith position.
            prefixSum += n
            # Get the remainder of the current prefixSum.
            remainder = prefixSum % k
            # We need to increase the result before update the frequency table.
            # Because we are counting how many previous prefixSum have the same remainder.
            res += remainderFrq[remainder]
            # Update the frequency table.
            remainderFrq[remainder] += 1
        return res
