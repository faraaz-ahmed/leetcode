class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(0, len(costs)):
            costs[i].append(costs[i][1] - costs[i][0])
        costs = sorted(costs, key = lambda x: x[2])
        minimumCost = 0
        for i in range(0, len(costs)):
            if i < len(costs) / 2:
                minimumCost += costs[i][1]
            else:
                minimumCost += costs[i][0]
        return minimumCost
