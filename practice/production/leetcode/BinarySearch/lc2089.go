// 2089. Find Target Indices After Sorting Array
// Easy
// 1.5K
// 71
// Companies
// You are given a 0-indexed integer array nums and a target element target.

// A target index is an index i such that nums[i] == target.

// Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

// Example 1:

// Input: nums = [1,2,5,2,3], target = 2
// Output: [1,2]
// Explanation: After sorting, nums is [1,2,2,3,5].
// The indices where nums[i] == 2 are 1 and 2.
// Example 2:

// Input: nums = [1,2,5,2,3], target = 3
// Output: [3]
// Explanation: After sorting, nums is [1,2,2,3,5].
// The index where nums[i] == 3 is 3.
// Example 3:

// Input: nums = [1,2,5,2,3], target = 5
// Output: [4]
// Explanation: After sorting, nums is [1,2,2,3,5].
// The index where nums[i] == 5 is 4.
 

// Constraints:

// 1 <= nums.length <= 100
// 1 <= nums[i], target <= 100
// Accepted
// 129.1K
// Submissions
// 170.2K
// Acceptance Rate
// 75.9%

import (
	"sort"
)
func targetIndices(nums []int, target int) []int {
	sort.Ints(nums)
	start, end := 0, len(nums) - 1
	index := -1
	for start <= end {
			mid := start + (end - start) / 2
			if (nums[mid] == target) {
					index = mid
					break
			} else if (nums[mid] < target) {
					start = mid + 1
			} else {
					end = mid - 1
			}
	}
	if (index == -1) {
			return make([]int, 0)
	}
	i := index - 1
	var result []int = make([]int, 0)
	result = append(result, index)
	for i >= 0 && nums[i] == target {
			result = append(result, i)
			i -= 1
	}
	i = index + 1
	for i < len(nums) && nums[i] == target {
			result = append(result, i)
			i += 1
	}
	sort.Ints(result)
	return result
}