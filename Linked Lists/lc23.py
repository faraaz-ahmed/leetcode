'''
23. Merge k Sorted Lists
Hard
16.5K
605
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
Accepted
1.6M
Submissions
3.2M
Acceptance Rate
49.6%
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


# class Solution:
#     # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#     def mergeTwoLists(self, headA, headB):
#         cursorA, cursorB = headA, headB
#         cursorC = headA
#         while True:
#             if cursorA and cursorB:
#                 if cursorB.val < cursorA.val:
#
#
#     def mergeKLists(self, lists):

