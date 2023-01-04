# 520. Detect Capital
# Easy
# 2.5K
# 410
# Companies
# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.


# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false


# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lenWord = len(word)
        if lenWord == 1:
            return True

        def isCap(s):
            return ord(s) >= 65 and ord(s) <= 90
        firstCap = isCap(word[0])
        allCaps = firstCap and isCap(word[1])
        if not firstCap and isCap(word[1]):
            return False
        for i in range(2, lenWord):
            if allCaps != isCap(word[i]):
                return False
        return True
