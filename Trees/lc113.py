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
        
        