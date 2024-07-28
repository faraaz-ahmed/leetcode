class BSTIterator:
  def __init__(self, root: TreeNode):
    self.root = root
    self.inorderList = self.getInorderList(root)

  def getInorderList(self, root):
    l = []
    if root:
      l += self.getInorderList(root.left)
      l += [root.val]
      l += self.getInorderList(root.right)
    return l

  def next(self) -> int:
    """
    @return the next smallest number
    """
    return self.inorderList.pop(0)
      
  def hasNext(self) -> bool:
    """
    @return whether we have a next smallest number
    """
    return True if len(self.inorderList) > 0 else False
