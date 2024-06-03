package Backtracking;

import java.util.ArrayList;
import java.util.List;

//class Solution:
//def partition(self, s: str) -> List[List[str]]:
//def is_palindrome(s):
//        return s == s[::-1]
//
//def backtrack(s, ans, candidates, start):
//        if start == len(s):
//        ans.append(list(candidates))
//        return
//        for i in range(start, len(s)):
//candidate = s[start:i+1]
//        if not is_palindrome(candidate):
//        continue
//        candidates.append(candidate)
//backtrack(s, ans, candidates, i + 1)
//                candidates.pop()
//ans = []
//candidates = []
//backtrack(s, ans, candidates, 0)
//        return ans
class lc131 {
    public static void main(String[] args) {
        
    }

    List<String> candidates;
    List<List<String>> answer;

    public Boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public void backtrack(String s, int start) {
        if (start == s.length() && candidates.size() > 0) {
            answer.add(new ArrayList<>(candidates));
        }
        for (int i = start; i < s.length(); i++) {
            String subStr = s.substring(start, i + 1);
            if (!isPalindrome(subStr)) {
                continue;
            }
            candidates.add(subStr);
            backtrack(s, i + 1);
            candidates.remove(candidates.size() - 1);
        }
    }

    public List<List<String>> partition(String s) {
        candidates = new ArrayList<>();
        answer = new ArrayList<>();
        int start = 0;
        backtrack(s, start);
        return answer;
    }
}