'''
101. Symmetric Tree
Easy
12.9K
288
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
Accepted
1.6M
Submissions
2.9M
Acceptance Rate
54.0%
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def imageInorder(self, root, isRightImage = False,  flag = ''):
        l = []
        if root:
            l += self.imageInorder(root.right if isRightImage else root.left, isRightImage, 'l')
            l.append(str(root.val) + flag)
            l += self.imageInorder(root.left if isRightImage else root.right, isRightImage, 'r')
        return l

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.imageInorder(root.left) == self.imageInorder(root.right, True)