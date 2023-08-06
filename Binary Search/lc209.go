/*
209. Minimum Size Subarray Sum
Medium
11.3K
316
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
*/

func binarySearch(nums []int, start int, end int, target int) int {
  for start <= end {
    mid := start + (end - start) / 2
    if (nums[mid] == target) {
      return mid
    } else if (nums[mid] < target) {
      start = mid + 1
    } else {
      end = mid - 1
    }
  }
  if (start >= len(nums)) {
    return -1
  }
  if (nums[start] > target) {
    return start
  }
  if (start + 1 >= len(nums)) {
    return -1
  }
  return start + 1
}
func minSubArrayLen(target int, nums []int) int {
  sumArr := make([]int, 0)
  sum_ := nums[0]
  length := len(nums)
  sumArr = append(sumArr, sum_)
  for i := 1; i < length; i++ {
    sum_ += nums[i]
    sumArr = append(sumArr, sum_)
  }
  if (length == 1) {
    if (nums[0] >= target) {
      return 1
    }
    return 0
  }
  minLength := binarySearch(sumArr, 0, length - 1, target) + 1
  if (minLength == -1) {
    minLength = length + 1
  }
  for i := 1; i < length; i++ {
    index := binarySearch(sumArr, i, length - 1, target + sumArr[i - 1]) + 1
    if (index >= i && index - i < minLength) {
      minLength = index - i
    }
  }
  if (minLength == length + 1) {
    return 0
  }
  return minLength
}