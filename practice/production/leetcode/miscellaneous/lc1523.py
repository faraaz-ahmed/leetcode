'''
1523. Count Odd Numbers in an Interval Range
Easy
1.8K
114
Companies
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9
Accepted
216.5K
Submissions
452K
Acceptance Rate
47.9%
'''


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff == 1:
            return diff
        if (low % 2 == 0 and not diff % 2 == 0) or (not low % 2 == 0):
            return (diff // 2) + 1
        return diff // 2
