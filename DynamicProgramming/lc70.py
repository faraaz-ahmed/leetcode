class Solution:
  def climbStairs(self, n: int) -> int:
    if n == 0:
      return 0
    one, total, previous_total = 1, 1, 1
    for i in range(1, n):
      previous_total = total
      total = total + one
      one = previous_total
    return total
