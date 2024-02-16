/*
1481. Least Number of Unique Integers after K Removals
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
*/

class Solution {
  public int findLeastNumOfUniqueInts(int[] arr, int k) {
      HashMap<Integer, Integer> frequencyMap = new HashMap<>();
      for (int n : arr) frequencyMap.put(n, frequencyMap.getOrDefault(n, 0) + 1);
      int removedCount = 0;
      Integer[] list = frequencyMap.values().toArray(new Integer[0]);
      Arrays.sort(list);
      for (int i = 0; i < list.length; i++) {
          if (k >= list[i]) {
              k -= list[i];
              removedCount += 1;
          } else {
              break;
          }
      }
      return list.length - removedCount;
  }
}