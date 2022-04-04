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
