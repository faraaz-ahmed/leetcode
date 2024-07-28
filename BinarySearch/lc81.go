// 81. Search in Rotated Sorted Array II
// Medium
// 6.6K
// 865
// Companies
// There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

// Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

// Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

// You must decrease the overall operation steps as much as possible.

 

// Example 1:

// Input: nums = [2,5,6,0,0,1,2], target = 0
// Output: true
// Example 2:

// Input: nums = [2,5,6,0,0,1,2], target = 3
// Output: false
 

// Constraints:

// 1 <= nums.length <= 5000
// -104 <= nums[i] <= 104
// nums is guaranteed to be rotated at some pivot.
// -104 <= target <= 104


func binarySearch(nums []int, start, end, target int) int {
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
func search(nums []int, target int) bool {
    index := 0
    for i := 0; i < len(nums) - 1; i++ {
        if (nums[i] > nums[i + 1]) {
            index = i + 1
            break
        }
    }
    if (binarySearch(nums, 0, index - 1, target) >= 0 || binarySearch(nums, index, len(nums) - 1, target) >= 0) {
        return true
    }
    return false
}