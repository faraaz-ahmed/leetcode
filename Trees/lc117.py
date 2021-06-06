class Solution:
  def connect(self, root: 'Node') -> 'Node':
    if root == None:
        return root
    queue, i = [root, '#'], 0
    while i < len(queue):
      if queue[i] == '#':
        if i == len(queue) - 1:
          break
        queue.append('#')
        i += 1
      node = queue[i]
      if queue[i].left:
        queue.append(queue[i].left)
      if queue[i].right:
        queue.append(queue[i].right)
      # queue.append('#')
      i += 1
    for i in range(0, len(queue) - 1):
      if queue[i + 1] == '#':
        queue[i].next = None
      else:
        if not queue[i] == '#':
          queue[i].next = queue[i + 1]
    return root
