'''
109. Convert Sorted List to Binary Search Tree
Medium
6.6K
141
Companies
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
Accepted
461.3K
Submissions
771.2K
Acceptance Rate
59.8%
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getArrayFromLinkedList(self, head):
        cursor = head
        arr = []
        while cursor:
            arr.append(cursor.val)
            cursor = cursor.next
        return arr

    def getBST(self, arr, node):
        if len(arr) == 0:
            return None
        mid = (len(arr) - 1) // 2
        node.val = arr[mid]
        node.left = self.getBST(arr[:mid], TreeNode())
        node.right = self.getBST(arr[mid + 1:], TreeNode())
        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.getBST(self.getArrayFromLinkedList(head), TreeNode())
