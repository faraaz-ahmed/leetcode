# 653.
# Two
# Sum
# IV - Input is a
# BST
# Easy
# 5.1
# K
# 224
# Companies
# Given
# the
# root
# of
# a
# Binary
# Search
# Tree and a
# target
# number
# k,
# return true if there
# exist
# two
# elements in the
# BST
# such
# that
# their
# sum is equal
# to
# the
# given
# target.
#
# Example
# 1:
#
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 9
# Output: true
# Example
# 2:
#
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 28
# Output: false
#
# Constraints:
#
# The
# number
# of
# nodes in the
# tree is in the
# range[1, 104].
# -104 <= Node.val <= 104
# root is guaranteed
# to
# be
# a
# valid
# binary
# search
# tree.
# -105 <= k <= 105
# Accepted
# 400
# K
# Submissions
# 659.4
# K
# Acceptance
# Rate
# 60.7 %

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    def dfs(memo, root, k):
      if root:
        if k - root.val in memo:
          return True
        memo[root.val] = 1
        return dfs(memo, root.left, k) or dfs(memo, root.right, k)
      return False

    return dfs({}, root, k)
