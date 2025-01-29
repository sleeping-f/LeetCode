# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def addTwoNumbers2(l1, l2, level = 0, sum = 0):
            if l1 !=  None and l2 != None:
                return (10**level) * (l1.val + l2.val) + addTwoNumbers2(l1.next, l2.next, level + 1)    
            elif l1 == None and l2 != None:
                return (10**level) * l2.val + addTwoNumbers2(l1, l2.next, level + 1)
            elif l1 != None and l2 == None:
                print(l1, l2)
                return (10**level) * l1.val + addTwoNumbers2(l1.next, l2, level + 1)
            else: return 0

        sum = addTwoNumbers2(l1, l2)
        ans = ListNode(sum%10)
        sum = sum // 10
        temp = ans
        while sum > 0:
            temp.next = ListNode(sum%10)
            sum = sum // 10
            temp = temp.next
        return ans