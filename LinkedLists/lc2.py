# Definition for singly-linked list.# class ListNode:#     def __init__(self, val=0, next=None):#         self.val = val#         self.next = nextclass Solution:    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        def getNum(l):            num, i, temp = 0, 0, l            while (temp != None):                num += temp.val * 10**i                temp = temp.next                i += 1            return num        sum_ = getNum(l1) + getNum(l2)        result = ListNode(0)        temp = result        while sum_ > 0:            temp.next = ListNode(sum_ % 10)            sum_ = int(sum_ // 10)            temp = temp.next        return result.next if result.next else result