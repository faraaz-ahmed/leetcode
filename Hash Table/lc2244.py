# 2244. Minimum Rounds to Complete All Tasks
# Medium
# 1.4K
# 39
# Companies
# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.


# Example 1:

# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2.
# - In the second round, you complete 2 tasks of difficulty level 3.
# - In the third round, you complete 3 tasks of difficulty level 4.
# - In the fourth round, you complete 2 tasks of difficulty level 4.
# It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
# Example 2:

# Input: tasks = [2,3,3]
# Output: -1
# Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.


# Constraints:

# 1 <= tasks.length <= 105
# 1 <= tasks[i] <= 109
# Accepted
# 71.9K
# Submissions
# 114.6K
# Acceptance Rate
# 62.7%

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        memo = {}

        def getRounds(num):
            rem = num % 3
            numOfThrees = num // 3
            return numOfThrees if rem == 0 else numOfThrees + 1
        for i in range(0, len(tasks)):
            if not tasks[i] in memo:
                memo[tasks[i]] = 1
            else:
                memo[tasks[i]] += 1
        counter = 0
        for key in memo.keys():
            if memo[key] == 1:
                return -1
            else:
                counter += getRounds(memo[key])
        return counter
