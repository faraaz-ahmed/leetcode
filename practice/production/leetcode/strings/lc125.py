'''
125. Valid Palindrome
Easy
6.1K
6.7K
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
Accepted
1.8M
Submissions
4.1M
Acceptance Rate
44.2%
'''

class Solution:
  def filterString(self, s):
    i = 0
    while i < len(s):
      if (ord(s[i]) < ord('a') or ord(s[i]) > ord('z')) and (ord(s[i]) < ord('0') or ord(s[i]) > ord('9')):
        s = s[:i] + s[i + 1:]
      else:
        i += 1
    return s

  def isPalindrome(self, s):
    s = self.filterString(s.lower())
    i, j = 0, len(s) - 1
    while i <= j:
      if s[i] == s[j]:
        i += 1
        j -= 1
        continue
      else:
        return False
    return True
