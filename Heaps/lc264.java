//264. Ugly Number II//        Solved//        Medium//        Topics//        Companies//        Hint//        An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.////        Given an integer n, return the nth ugly number.////////        Example 1:////        Input: n = 10//        Output: 12//        Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.//        Example 2:////        Input: n = 1//        Output: 1//        Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.//////        Constraints:////        1 <= n <= 1690package Heaps;import java.util.HashSet;import java.util.PriorityQueue;import java.util.Queue;import java.util.Set;public class lc264 {    class Solution {        public int nthUglyNumber(int n) {            Queue<Long> heap = new PriorityQueue<>();            Set<Long> uglyNumberSet = new HashSet<>();            Long currentUglyNumber = 1L;            int[] factors = {2, 3, 5};            int uglyNumberCount = 1;            while (uglyNumberCount < n) {                for (int factor: factors) {                    Long uglyNumber = factor * currentUglyNumber;                    if (!uglyNumberSet.contains(uglyNumber)) {                        uglyNumberSet.add(uglyNumber);                        heap.add(uglyNumber);                    }                }                currentUglyNumber = heap.remove();                uglyNumberCount += 1;            }            return Math.toIntExact(currentUglyNumber);        }    }}