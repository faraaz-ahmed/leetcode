/**
34. Find First and Last Position of Element in Sorted Array
Medium
18.8K
453
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
Accepted
1.7M
Submissions
4M
Acceptance Rate
42.8%
*/

func findIndex(nums []int, target int, start int, end int) int {
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
	return -1
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func searchRange(nums []int, target int) []int {
  result := make([]int, 0, 2)
  lenNums := len(nums)
  index := findIndex(nums, target, 0, lenNums - 1)
  if (-1 == index) {
    result = append(result, -1)
    result = append(result, -1)
  } else {
    i, j := index, index
    for i - 1 >= 0 && nums[i - 1] == target {
      i -= 1
    }
    for j + 1 < len(nums) && (nums[j + 1] == target) {
      j += 1 
    }
    result = append(result, max(0,i))
    result = append(result, min(len(nums) - 1, j))
  }
  return result
}