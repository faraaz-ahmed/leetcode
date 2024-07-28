'''
6. Zigzag Conversion
Medium
5.2K
10.9K
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
Accepted
930.5K
Submissions
2.1M
Acceptance Rate
43.8%
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        matrix = []
        for i in range(0, numRows):
            matrix.append([])
        lenS = len(s)
        ascend = False
        i = 0
        while i < lenS:
            if not ascend:
                j = 0
                while j < numRows and i < lenS:
                    matrix[j].append(s[i])
                    j += 1
                    i += 1
            else:
                j = numRows - 2
                while j > 0 and i < lenS:
                    matrix[j].append(s[i])
                    j -= 1
                    i += 1
            ascend = not ascend
        result = ''
        for i in range(0, len(matrix)):
            result += ''.join(matrix[i])
        return result
