// 441. Arranging Coins
// Easy
// 3.5K
// 1.3K
// Companies
// You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

// Given the integer n, return the number of complete rows of the staircase you will build.

 

// Example 1:


// Input: n = 5
// Output: 2
// Explanation: Because the 3rd row is incomplete, we return 2.
// Example 2:


// Input: n = 8
// Output: 3
// Explanation: Because the 4th row is incomplete, we return 3.
 

// Constraints:

// 1 <= n <= 231 - 1

func arrangeCoins(n int) int {
	start, end := 0, n - 1
	if (n == 1) {
			return 1
	}
	for start <= end {
			mid := start + (end - start) / 2
			sum := mid * (mid + 1) / 2
			if (sum == n) {
					return mid
			} else if (sum < n) {
					start = mid + 1
			} else {
					end = mid - 1
			}
	}
	return start - 1
}