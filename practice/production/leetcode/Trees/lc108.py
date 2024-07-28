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
      elif val > root.val:
        if root.right:
          self.insert(root.right, val)
        else:
          root.right = TreeNode(val)
  def inserter(self, root, nums):
    if len(nums) > 0:
      mid = len(nums) // 2
      self.insert(root, nums[mid])
      self.inserter(root, nums[:mid])
      self.inserter(root, nums[mid + 1:])
    
    
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    mid = nums[len(nums) // 2]
    root = TreeNode(mid)
    self.inserter(root, nums)
    return root
        