'''1137. N-th Tribonacci Number
Easy
2.6K
136
Companies
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
Accepted
389.9K
Submissions
615.3K
Acceptance Rate
63.4%'''


class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        t3 = 0
        for i in range(3, n + 1):
            t3 = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t3
        return t3
