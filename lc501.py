# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getList(self, root: TreeNode):
        if root:
            return self.getList(root.left) + [root.val] + self.getList(root.right)
        return []
            
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        l = self.getList(root)
        d = {}
        for i in range(0, len(l)):
            if l[i] in d:
                d[l[i]] += 1
            else:
                d[l[i]] = 1
        max_ = max(d.values())
        l = []
        for key in d.keys():
            if d[key] == max_:
                l.append(key)
        return l
            
        
