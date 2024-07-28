'''2359. Find Closest Node to Given Two Nodes
Medium
1.3K
309
Companies
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

 

Example 1:


Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:


Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
 

Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
Accepted
57.8K
Submissions
125.9K
Acceptance Rate
45.9%'''


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def getDistanceMap(cur, distanceMap):
            distance = 0
            while (not cur in distanceMap) and (not cur == -1):
                distance += 1
                distanceMap[cur] = distance
                cur = edges[cur]
            return distanceMap
        distanceMap1, distanceMap2 = getDistanceMap(
            edges[node1], {node1: 0}), getDistanceMap(edges[node2], {node2: 0})
        distanceSum = {}
        for key in distanceMap1.keys():
            if key in distanceMap2:
                distanceSum[key] = max(distanceMap1[key], distanceMap2[key])
        distanceSumKeys = list(distanceSum.keys())
        if len(distanceSumKeys) == 0:
            return -1
        minKey = distanceSumKeys[0]
        for i in range(1, len(distanceSumKeys)):
            if (distanceSum[distanceSumKeys[i]] == distanceSum[minKey]) and (distanceSumKeys[i] < minKey):
                minKey = distanceSumKeys[i]
            elif distanceSum[distanceSumKeys[i]] < distanceSum[minKey]:
                minKey = distanceSumKeys[i]
        return minKey
