//# 290. Word Pattern
//        # Easy
//        # 4.5K
//        # 520
//        # Companies
//        # Given a pattern and a string s, find if s follows the same pattern.
//
//        # Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
//
//
//        # Example 1:
//
//        # Input: pattern = "abba", s = "dog cat cat dog"
//        # Output: true
//        # Example 2:
//
//        # Input: pattern = "abba", s = "dog cat cat fish"
//        # Output: false
//        # Example 3:
//
//        # Input: pattern = "aaaa", s = "dog cat cat dog"
//        # Output: false
//
//
//        # Constraints:
//
//        # 1 <= pattern.length <= 300
//        # pattern contains only lower-case English letters.
//        # 1 <= s.length <= 3000
//        # s contains only lowercase English letters and spaces ' '.
//        # s does not contain any leading or trailing spaces.
//        # All the words in s are separated by a single space.
//        # Accepted
//        # 423.3K
//        # Submissions
//        # 1M
//        # Acceptance Rate
//        # 40.6%


import java.util.HashMap;
class lc290 {
    class Solution {

        public boolean wordPattern(String pattern, String s) {
            String[] strArr = s.split(" ");
            HashMap<String, String> map = new HashMap<>();
            HashMap<String, String> patternSoFar = new HashMap<>();
            if (pattern.length() != strArr.length) {
                return false;
            }
            for (int i = 0; i < strArr.length; i++) {
                if (map.containsKey(strArr[i])) {
                    if (!map.get(strArr[i]).equals(String.valueOf(pattern.charAt(i)))) {
                        return false;
                    }
                } else if (patternSoFar.containsKey(String.valueOf(pattern.charAt(i)))) {
                    return false;
                } else {
                    patternSoFar.put(String.valueOf(pattern.charAt(i)), "present");
                    map.put(strArr[i], String.valueOf(pattern.charAt(i)));
                }
            }
            return true;
        }
    }
}