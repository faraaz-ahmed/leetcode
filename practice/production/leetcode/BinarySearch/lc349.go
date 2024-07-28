// 349. Intersection of Two Arrays
// Easy
// 5K
// 2.2K
// Companies
// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.
 

// Constraints:

// 1 <= nums1.length, nums2.length <= 1000
// 0 <= nums1[i], nums2[i] <= 1000
// Accepted
// 890.1K
// Submissions
// 1.2M
// Acceptance Rate
// 71.4%

import (
	"fmt"
	"sort"
)

func binarySearch(nums []int, number int) int {
	start, end := 0, len(nums) - 1
	for start <= end {
		mid := start + (end - start) / 2
		if (nums[mid] == number) {
			return mid
		} else if (nums[mid] < number) {
			start = mid + 1
		} else {
			end = mid - 1
		}
	}
	return -1
}

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func intersection(nums1 []int, nums2 []int) []int {
	sort.Ints(nums2)
	var result = []int{}
	index := 0
	for i := 0; i < len(nums1); i++ {
		if (binarySearch(nums2, nums1[i]) >= 0) {
			if (!contains(result, nums1[i])) {
				result=append(result,nums1[i])
			}
			index += 1
		}
	}
	return result
}