'''
279. Perfect Squares
Solved
Medium
Topics
Companies
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
'''

class Solution:
    def numSquares(self, n: int) -> int:
      global dp
      dp = { 0:0, 1:1, 2:2, 3:3, 4:1 }
      squares = []
      for i in range(1, n):
        square = i * i
        if square <= n:
          squares.append(square)
      def getResult(n):
        if n in dp:
          return dp[n]
        elif math.sqrt(n).is_integer():
          return 1
        min_ = 0
        for square in squares:
          if n - square > 0:
            res = getResult(n - square)
            current = 0 if res == 0 else (1 + res) 
            if (min_ > current) or (min_ == 0 and current > 0):
              min_ = current
        dp[n] = min_
        return dp[n]
      return getResult(n)
        