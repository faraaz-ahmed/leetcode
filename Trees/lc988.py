# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPaths(self, root: TreeNode) -> list:
        list_ = []
        if root:
            left = self.getPaths(root.left)
            right = self.getPaths(root.right)
            for i in range(0, len(left)):
                left[i] += chr(97 + root.val)
            for i in range(0, len(right)):
                right[i] += chr(97 + root.val)
            if left == [] and right == []:
                return [chr(97 + root.val)]
            list_ = left + right
        return list_
    def smallestFromLeaf(self, root: TreeNode) -> str:
        return min(self.getPaths(root))
            
            
