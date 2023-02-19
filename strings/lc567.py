'''
567. Permutation in String
Medium
8.1K
267
Companies
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
Accepted
547.5K
Submissions
1.3M
Acceptance Rate
43.5%
'''


class Solution:
    def createMap(self):
        mapp = {}
        for i in range(0, 26):
            mapp[chr(i + 97)] = 0
        return mapp

    def checkWithS1(self, mappS1, mapp):
        keys = mappS1.keys()
        for key in keys:
            if not key in mapp or not mapp[key] == mappS1[key]:
                return False
        return True

    def populateMap(self, strr, mapp):
        for s in strr:
            if not s in mapp:
                mapp[s] = 1
            else:
                mapp[s] += 1
        return mapp

    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = self.createMap()
        i, j = 0, len(s1) - 1
        mapp = self.populateMap(s2[:len(s1)], mapp)
        mappS1 = {}
        for s in s1:
            if not s in mappS1:
                mappS1[s] = 1
            else:
                mappS1[s] += 1
        while j < len(s2):
            if self.checkWithS1(mappS1, mapp):
                return True
            if not s2[i] in mapp:
                mapp[s2[i]] = 1
            else:
                mapp[s2[i]] -= 1
            i += 1
            j += 1
            if j < len(s2):
                if not s2[j] in mapp:
                    mapp[s2[j]] = 1
                else:
                    mapp[s2[j]] += 1
        return False
