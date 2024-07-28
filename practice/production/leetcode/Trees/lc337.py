# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def robSub(self, root: TreeNode, dict_) -> int:
        if root in dict_:
            return dict_[root]
        val = 0
        if root:
            if root.left:
                val += self.robSub(root.left.left, dict_) + self.robSub(root.left.right, dict_)
            if root.right:
                val += self.robSub(root.right.left, dict_) + self.robSub(root.right.right, dict_)
            val = max(val + root.val, self.robSub(root.left, dict_) + self.robSub(root.right, dict_))
            dict_[root] = val
        return val
    def rob(self, root: TreeNode) -> int:
        return self.robSub(root, {})
