/*
1346. Check If N and Its Double Exist
Easy
1.7K
184
Companies
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
*/

import (
  "sort"
)

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
  return -1
}

func checkIfExist(arr []int) bool {
  index := -1
  length := len(arr)
  sort.Ints(arr)
  for i := 0; i < len(arr); i++ {
    if (arr[i] < 0 && arr[i] % 2 == 0) {
      index = binarySearch(arr, i + 1, length - 1, arr[i] / 2)
    } else {
      index = binarySearch(arr, i + 1, length - 1, arr[i] * 2)
    }
    if (index >= 0) {
      return true
    }
  }
  return false
}