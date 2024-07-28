'''
28. Find the Index of the First Occurrence in a String
Medium
2.7K
135
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
Accepted
1.6M
Submissions
4.2M
Acceptance Rate
38.7%
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        stack = list(needle)
        counter, i = 0, 0
        while i < len(haystack):
            if len((stack)) == 0:
                return i - len(needle)
            if stack[0] == haystack[i]:
                stack.pop(0)
                counter += 1
            else:
                i = i - counter + 1
                counter = 0
                stack = list(needle)
                continue
            i += 1
        if len((stack)) == 0:
            return i - len(needle)
        return -1
