# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root, val):
        if root:
            if val < root.val:
                if root.left:
                    self.insert(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if  root.right:
                    self.insert(root.right, val)
                else:
                    root.right = TreeNode(val)
                
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        self.insert(root, val)
        if not root:
            root = TreeNode(val)
        return root
