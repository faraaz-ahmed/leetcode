'''
264. Ugly Number II
Solved
Medium
Topics
Companies
Hint
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


Constraints:

1 <= n <= 1690
'''
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        current_ugly_number = 1
        ugly_number_count = 1
        factors = [1, 2, 3]
        ugly_number_set = {1}

        while ugly_number_count < n:
            for factor in factors:
                ugly_number = factor * current_ugly_number
                if ugly_number not in ugly_number_set:
                    heapq.heappush(heap, ugly_number)
                    ugly_number_set.add(ugly_number)
            current_ugly_number = heapq.heappop(heap)
            ugly_number_count += 1

        return current_ugly_number