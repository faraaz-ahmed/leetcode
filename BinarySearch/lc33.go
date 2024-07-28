// 33. Search in Rotated Sorted Array
// Medium
// 22.7K
// 1.3K
// Companies
// There is an integer array nums sorted in ascending order (with distinct values).

// Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

// Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

// You must write an algorithm with O(log n) runtime complexity.

 

// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
// Example 2:

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1
// Example 3:

// Input: nums = [1], target = 0
// Output: -1
 

// Constraints:

// 1 <= nums.length <= 5000
// -104 <= nums[i] <= 104
// All values of nums are unique.
// nums is an ascending array that is possibly rotated.
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
func search(nums []int, target int) int {
    index := 0
    for i := 0; i < len(nums) - 1; i++ {
        if (nums[i] > nums[i + 1]) {
            index = i + 1
            break
        }
    }
    leftIndex, rightIndex := binarySearch(nums, 0, index - 1, target), binarySearch(nums, index, len(nums) - 1, target)
    if (leftIndex >= 0) {
        return leftIndex
    }
    if (rightIndex >= 0) {
        return rightIndex
    }
    return -1
}