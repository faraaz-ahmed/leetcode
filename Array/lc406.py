class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for i in range(0, len(people)):
            res.insert(people[i][1], people[i])
        return res
