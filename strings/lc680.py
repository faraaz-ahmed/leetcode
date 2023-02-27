'''
680. Valid Palindrome II
Easy
6.9K
359
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
Accepted
578.2K
Submissions
1.5M
Acceptance Rate
39.3%
'''

class Solution:
  def isPalindrome(self, s):
    i, j = 0, len(s) - 1
    while i <= j:
      if s[i] == s[j]:
        i += 1
        j -= 1
        continue
      else:
        return False
    return True

  def validPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1
    while i <= j:
      if s[i] == s[j]:
        i += 1
        j -= 1
        continue
      else:
        return self.isPalindrome(s[i: j]) or self.isPalindrome(s[i + 1: j + 1])
    return True

#
sol = Solution()
print(sol.validPalindrome("okko"))
print(sol.validPalindrome("okrrkio"))
print(sol.validPalindrome("okrriko"))
print(sol.validPalindrome("okrirko"))
print(sol.validPalindrome("okirrko"))
print(sol.validPalindrome("oikrrko"))
print(sol.validPalindrome("iokrrko"))
print(sol.validPalindrome("okrrkiio"))

