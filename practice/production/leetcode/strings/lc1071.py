'''1071. Greatest Common Divisor of Strings
Easy
1.6K
321
Companies
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            big = str1
            small = str2
        else:
            big = str2
            small = str1
        lenBig, lenSmall = len(big), len(small)
        divisor = small
        lenDivisor = lenSmall
        while lenDivisor > 0:
            if lenBig % lenDivisor == 0:
                if big == divisor * (lenBig // lenDivisor):
                    if lenSmall % lenDivisor == 0:
                        if small == divisor * (lenSmall // lenDivisor):
                            return divisor
            divisor = divisor[:-1]
            lenDivisor -= 1
        return ''
