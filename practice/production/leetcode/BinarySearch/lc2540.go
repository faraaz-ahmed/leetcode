// 2540. Minimum Common Value
// Easy
// 421
// 9
// Companies
// Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

// Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

// Example 1:

// Input: nums1 = [1,2,3], nums2 = [2,4]
// Output: 2
// Explanation: The smallest element common to both arrays is 2, so we return 2.
// Example 2:

// Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
// Output: 2
// Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 

// Constraints:

// 1 <= nums1.length, nums2.length <= 105
// 1 <= nums1[i], nums2[j] <= 109
// Both nums1 and nums2 are sorted in non-decreasing order.

func search(nums []int, target int) int {
	start, end := 0, len(nums) - 1
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
func getCommon(nums1 []int, nums2 []int) int {
	for i := 0; i < len(nums1); i++ {
			if (search(nums2, nums1[i]) >= 0) {
					return nums1[i]
			}
	}
	return -1
}