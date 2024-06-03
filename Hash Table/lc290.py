# 290. Word Pattern
# Easy
# 4.5K
# 520
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# Accepted
# 423.3K
# Submissions
# 1M
# Acceptance Rate
# 40.6%


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        memo = {}
        patternSoFar = {}
        arrStr = s.split()
        if not len(arrStr) == len(pattern):
            return False
        for i in range(0, len(arrStr)):
            if arrStr[i] in memo:
                if not memo[arrStr[i]] == pattern[i]:
                    return False
            elif pattern[i] in patternSoFar:
                return False
            else:
                patternSoFar[pattern[i]] = 'present'
                memo[arrStr[i]] = pattern[i]
        return True






