class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # use dynamice programming dp[i] = min(dp[i - 1] + cost, dp[i - 2] + cost[i - 2])
        # last and lastsecond are records of getting to last and previous last ith location respectively
        last, lastsecond, present = 0, 0, 0
        for i in range(2, len(cost) + 1):
            present = min(last + cost[i - 1], lastsecond + cost[i - 2])
            lastsecond = last
            last = present
        return present