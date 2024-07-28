# 113. Path Sum II
# Medium

# 5709

# 122

# Add to List

# Share
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
# Accepted
# 647,447
# Submissions
# 1,164,517



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def copy(self, arr):
    res = []
    for item in arr:
      itemCopy = item
      if isinstance(item, list) and len(item) > 0:
        itemCopy = self.copy(item)
      res.append(itemCopy)
    return res
  
  def computeResult(self, arr, root):
    if len(arr) == 0:
      arr.append([root.val])
    else:
      for res in arr:
        res.append(root.val)
    return arr
        
  def isLeaf(self, root):
    return (not root.left) and (not root.right)
  
  def getPathSum(self, root: TreeNode, result, targetSum: int):
    if root:
      shouldComputeResultsAndReturn = False
      if self.isLeaf(root) and targetSum - root.val == 0:
        shouldComputeResultsAndReturn = True
      elif self.isLeaf(root) and (not targetSum - root.val == 0):
        return False
      resultCopy = self.copy(self.computeResult(self.copy(result), root))
      if shouldComputeResultsAndReturn:
        return resultCopy
      left, right = self.getPathSum(root.left, resultCopy, targetSum - root.val), self.getPathSum(root.right, resultCopy, targetSum - root.val)
      return (left if not left == False else []) + (right if not right == False else [])
    return []
  
  def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
    if not root:
      return []
    if (not root.left) and (not root.right):
      return [[root.val]] if root.val == targetSum else []
    return self.getPathSum(root, [], targetSum)
        

#Attempt 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if root:
      if targetSum - root.val == 0 and (not root.left) and (not root.right):
        return [[root.val]]
      left = self.pathSum(root.left, targetSum - root.val)
      right = self.pathSum(root.right, targetSum - root.val)
      def processNode(node):
        if node and len(node) > 0:
          for i in range(len(node)):
            node[i].insert(0, root.val)
        return node
      left = processNode(left)
      right = processNode(right)
      if left == None and right == None:
        return None
      elif left == None:
        return right
      elif right == None:
        return left
      else:
        return left + right
        