 /*
 169. Majority Element
Solved
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
 */

class Solution {
  public int majorityElement(int[] nums) {
      int count = 1;
      int candidate = nums[0];
      // iterate and find the majority candidate
      for(int i = 1; i < nums.length; i++) {
        if (nums[i] == candidate) {
          count += 1;
        } else {
          count -= 1;
        }
        if (count == 0) {
          candidate = nums[i];
          count = 1;
        }
      }
      // verifying cadidate eligibility
      int frequency = 0;
      for (int i = 0; i < nums.length; i++) {
        if (nums[i] == candidate) {
          frequency++;
        }
      }
      if (frequency > Math.floor(nums.length / 2)) {
        return candidate;
      } else {
        // should never happen since test cases always have a valid candidate
        return 0;
      }
  }
}

