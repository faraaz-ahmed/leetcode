# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        str_ = []
        if root:
            if not root.left and not root.right:
                return [str(root.val)]
            left = self.binaryTreePaths(root.left)
            right = self.binaryTreePaths(root.right)
            for i in range(0, len(left)):
                left[i] = str(root.val) + '->' + left[i]
            for i in range(0, len(right)):
                right[i] = str(root.val) + '->' + right[i]
            return left + right
        return str_
            
            
