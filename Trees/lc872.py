# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


# Example 1:
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# Example 2:
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false


# Constraints:

# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getLeaves(self, root):
        if root:
            leaves = []
            if root.left == None and root.right == None:
                return [root.val]
            else:
                leaves = (self.getLeaves(root.left) if root.left else []) + (self.getLeaves(root.right) if root.right else [])
            return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1, arr2 = self.getLeaves(root1), self.getLeaves(root2)
        i = len(arr1) - 1
        if not len(arr1) == len(arr2):
            return False
        else:
            while i >= 0:
                if not arr1[i] == arr2[i]:
                    return False
                i -= 1
        return True
