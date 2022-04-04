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

