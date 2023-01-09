# 144. Binary Tree Preorder Traversal
# Easy
# 6.2K
# 164
# Companies
# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Follow up: Recursive solution is trivial, could you do it iteratively?

# Accepted
# 1.2M
# Submissions
# 1.8M
# Acceptance Rate
# 66.1%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        if root:
            l.append(root.val)
            l += self.preorderTraversal(root.left) + \
                self.preorderTraversal(root.right)
        return l
