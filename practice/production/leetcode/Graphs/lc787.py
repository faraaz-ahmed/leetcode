'''787. Cheapest Flights Within K Stops
Medium
7.3K
319
Companies
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.



Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for i in range(0, len(flights)):
            if not flights[i][0] in graph:
                graph[flights[i][0]] = [flights[i][1:]]
            else:
                graph[flights[i][0]].append(flights[i][1:])
        dfsMap, visited = {}, {}
        def dfs(node, graph, dst, k, cost, depth):
            nonlocal dfsMap
            nonlocal visited
            if k >= depth and not node in visited:
                visited[node] = 1
                depth += 1
                if node == dst:
                    return [cost, depth]
            else:
                return [-1, -1]
            if node in graph:
                children = graph[node]
            else:
                return [-1, -1]
            for child in children:
                if child[0] in dfsMap:
                    cost += child[1]
                    return dfsMap[child[0]]
                else:
                    cost += child[1]
                    dfsMap[child[0]] = dfs(child[0], graph, dst, k, cost, depth)
                    return dfsMap[child[0]]
            return [-1, -1]
        dfs(src, graph, dst, k, 0, 0)
        print('check', graph, dfsMap)
        minCost = -1
        for key in dfsMap.keys():
            if not dfsMap[key][1] == -1 and (minCost > dfsMap[key][1] or minCost == -1):
                minCost = dfsMap[key][1]
        return minCost
