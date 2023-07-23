class Solution:
  def isPalindrome(self, head):
    if head == None:
        return True
    if head.next == None:
      return True
    temp = head
    x = []
    while not temp == None:
      x.append(temp.val)
      temp = temp.next
    x1, x2 = x[0: int(len(x) / 2)], x[int(len(x)/2): len(x)]
    if len(x2) > len(x1):
      x2.pop(0)
    x2.reverse()
    return x1 == x2