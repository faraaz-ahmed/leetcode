# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getStr(self, t: TreeNode) -> str:
        str_ = ''
        if t:
            left, right = self.getStr(t.left), self.getStr(t.right)
            str_ = str(t.val) + ('(' + left + ')' if (left == ''  and not right == '') else left) + right
        if str_ == '':
            return ''
        else:
            return '(' + str_ + ')'
    def tree2str(self, t: TreeNode) -> str:
        x = self.getStr(t)
        return x[1: len(x) - 1]
        
