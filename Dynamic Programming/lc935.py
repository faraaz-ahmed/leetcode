# 935. Knight Dialer
# Medium
# 2.8K
# 432
# Companies
# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

# A chess knight can move as indicated in the chess diagram below:


# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


# Given an integer n, return how many distinct phone numbers of length n we can dial.

# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

# As the answer may be very large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
# Example 2:

# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
# Example 3:

# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.
 

# Constraints:

# 1 <= n <= 5000
# Accepted
# 157K
# Submissions
# 266.1K
# Acceptance Rate
# 59.0%


class Solution:
  def knightDialer(self, n: int) -> int:
    modulo = 10**9+7
    dp = [[] for _ in range(n)]
    moves = {
      0: [4, 6],
      1: [6, 8],
      2: [7, 9],
      3: [4, 8],
      4: [3, 0, 9],
      5: [],
      6: [1, 7, 0],
      7: [2, 6],
      8: [1, 3],
      9: [2, 4]
    }

    for i in range(0, n):
      for j in range(0, 10):
        dp[i].append(1 if i == 0 else 0)

    for i in range(1, n):
      for j in range(0, 10):
        possible_moves = moves[j]
        for possible_move in possible_moves:
          dp[i][j] = (dp[i][j] + dp[i - 1][possible_move]) % modulo

    result = 0
    for item in dp[n - 1]:
      result = (result + item) % modulo
    return result


        