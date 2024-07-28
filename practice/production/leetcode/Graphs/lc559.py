"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        d = 0
        if root:
            if len(root.children) > 0:
                maxDepth = self.maxDepth(root.children[0])
                for i in range(1, len(root.children)):
                    childDepth = self.maxDepth(root.children[i])
                    if maxDepth < childDepth:
                        maxDepth = childDepth
                d += (maxDepth + 1)
            else:
                d += 1
        return d
                
                
        
