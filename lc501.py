# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMode(self, root: TreeNode):
        l = [0]
        if root:
            if not root.left and not root.right:
                return [root.val, 1]
            left = self.getMode(root.left)
            right = self.getMode(root.right)
            print(right, root.val)
            if (left[len(left) - 1] == right[len(right) - 1]):
                if left[len(left) - 1] == 0:
                    return [root.val, 1]
                if left[len(left) - 1] == 1 and root.val not in left[:len(left) - 1] and root.val not in right[:len(right) - 1]:
                    return [root.val] + left[:len(left) - 1] + right
                right[len(right) - 1] += 1
                return left[:len(left) - 1] + right
            elif (left[len(left) - 1] > right[len(right) - 1]):
                if left[len(left) - 1] == 1 and root.val not in left[:len(left) - 1]:
                    return [root.val] + left
                return left
            else:
                if right[len(right) - 1] == 1 and root.val not in right[:len(right) - 1]:
                    return [root.val] + right
                return right
        return l
        
    def findMode(self, root: TreeNode) -> List[int]:
        x = self.getMode(root)
        return x[:len(x) - 1]
