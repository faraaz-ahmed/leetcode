// 611. Valid Triangle Number
// Medium
// 3.5K
// 192
// Companies
// Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

// Example 1:

// Input: nums = [2,2,3,4]
// Output: 3
// Explanation: Valid combinations are: 
// 2,3,4 (using the first 2)
// 2,3,4 (using the second 2)
// 2,2,3
// Example 2:

// Input: nums = [4,2,3,4]
// Output: 4
 

// Constraints:

// 1 <= nums.length <= 1000
0 <= nums[i] <= 1000
func binarySearch(nums []int, number int) int {
	// return index of searched element else return -1 if not found
	start, end := 0, len(nums)
	for start <= end {
		mid = start + (end - start) / 2
		if (nums[mid] == number) {
			return mid
		} else if (nums[mid] > number) {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return -1
}

// -------------- Solution below ---------------

import (
	"sort"
)

func getNumberOfLesserThan(nums []int, start int, number int) int {
	end := len(nums) - 1
	for start <= end {
		mid := start + (end - start) / 2
		if (nums[mid] >= number) {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return start
}

func triangleNumber(nums []int) int {
	sort.Ints(nums)
	sum := 0
	for i := 0; i < len(nums) - 2; i++ {
		for j := i + 1; j < len(nums) - 1; j++ {
			sum += getNumberOfLesserThan(nums, j + 1, nums[i] + nums[j]) - j - 1
		}
	}
	return sum
}