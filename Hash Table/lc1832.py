# #1832. Check if the Sentence Is Pangram
# Easy
# 1.1K
# 26
# Companies
# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
#
#
#
# Example 1:
#
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:
#
# Input: sentence = "leetcode"
# Output: false
#
#
# Constraints:
#
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
# Accepted
# 119.1K
# Submissions
# 145.8K
# Acceptance Rate
# 81.7%

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        memo = {}
        count = 26
        for i in range(0, len(sentence)):
            if not sentence[i] in memo:
                count -= 1
                if count == 0:
                    return True
                memo[sentence[i]] = 1
            else:
                memo[sentence[i]] += 1
        return False