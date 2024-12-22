'''
438. Find All Anagrams in a String
Medium
9.9K
296
Companies
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
Accepted
684.3K
Submissions
1.4M
Acceptance Rate
49.5%
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start, end = 0, len(p) - 1
        result = []

        def getMap(substr):
            mapp = {}
            for i in range(0, len(substr)):
                if not substr[i] in mapp:
                    mapp[substr[i]] = 1
                else:
                    mapp[substr[i]] += 1
            return mapp
        mapP = getMap(p)
        mapSubstr = {}

        def compareMaps(map1, map2):
            for key in map1.keys():
                if (not key in map2):
                    return False
                elif (not map2[key] == map1[key]):
                    return False
            return True
        while end < len(s):
            if mapSubstr == {}:
                mapSubstr = getMap(s[start:end + 1])
                if compareMaps(mapSubstr, mapP):
                    result.append(start)
            else:
                if s[start - 1] in mapSubstr:
                    mapSubstr[s[start - 1]] -= 1
                    if mapSubstr[s[start - 1]] == 0:
                        del mapSubstr[s[start - 1]]
                if not s[end] in mapSubstr:
                    mapSubstr[s[end]] = 1
                else:
                    mapSubstr[s[end]] += 1
                if compareMaps(mapP, mapSubstr):
                    result.append(start)
            start += 1
            end += 1
        return result
