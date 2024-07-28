'''
997. Find the Town Judge
Easy
5.1K
403
Companies
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
Accepted
374.9K
Submissions
755.4K
Acceptance Rate
49.6%
'''


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        memo = {}
        peopleMemo = {}
        if len(trust) == 0 and n == 1:
            return 1
        elif len(trust) == 0:
            return -1
        for i in range(0, len(trust)):
            if not trust[i][0] in peopleMemo:
                peopleMemo[trust[i][0]] = 1
            if not trust[i][1] in peopleMemo:
                peopleMemo[trust[i][1]] = 1
            if not trust[i][0] in memo:
                memo[trust[i][0]] = {trust[i][1]: 1}
            else:
                memo[trust[i][0]][trust[i][1]] = 1
        peopleKeys = peopleMemo.keys()
        if not len(peopleKeys) == n:
            return -1
        judge = -1
        for peopleKey in peopleKeys:
            if not peopleKey in memo and not judge == -1:
                return -1
            elif not peopleKey in memo:
                judge = peopleKey
        if judge == -1:
            return judge
        keys = memo.keys()
        for key in keys:
            if not judge in memo[key]:
                return -1
        return judge
