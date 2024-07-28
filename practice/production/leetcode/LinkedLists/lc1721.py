# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

  def getSize(self, head):
    size, temp = 0, head
    while not temp == None:
      size += 1
      temp = temp.next
    return size

  def getNthNode(self, head, n):
    temp, i = head, 0
    while (not temp == None):
      if i == n - 1:
        return temp
      else:
        i += 1
        temp = temp.next
    return None

  def getNthNodeEfficiently(self, head, k, size):
    temp, i = head, 0
    result = []
    while (not temp == None) and (not len(result) == 2) and (i < size):
      if i == k - 1:
        result.append(temp)
      elif i == size - k:
        result.append(temp)
      i += 1
      temp = temp.next
    if len(result) == 1:
      return [result[0], result[0]]
    return result

  def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    size = self.getSize(head)
    [temp1, temp2] = self.getNthNodeEfficiently(head, k, size)
    temp = temp1.val
    temp1.val = temp2.val
    temp2.val = temp
    return head