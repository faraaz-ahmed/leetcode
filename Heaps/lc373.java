package Heaps;import java.util.*;public class lc373 {    class Solution {        record Pair(int num1, int num2) {}        public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {            Queue<Pair> heap = new PriorityQueue<>(Comparator.comparingInt(x -> x.num1() + x.num2()));            for (int i = 1; i < nums2.length; i++)                heap.add(new Pair(nums1[0], nums2[i]));            List<List<Integer>> result = new ArrayList<>();            result.add(new ArrayList<>(List.of(nums1[0], nums2[0])));            while (result.size() < k) {                int i = 1, j = 0;                while (i < nums1.length && j < nums2.length) {                }//                for (int i = 0; i < nums2.length; i++) {//                    for (int j = 1; j < nums1.length; j++) {//                        Pair currentLowest = heap.remove();//                        if (nums2[i] + nums1[j] < currentLowest.num1() + currentLowest.num2()) {//                            result.add(new ArrayList<>(List.of(nums1[0], nums2[0])));//                            heap.add(currentLowest);//                        } else {//                            result.add(new ArrayList<>(List.of(currentLowest.num1(), currentLowest.num2())));//                        }//                    }//                }            }            return result;        }    }}