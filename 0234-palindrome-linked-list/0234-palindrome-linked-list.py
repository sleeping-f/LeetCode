# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        t = head
        back = None
        while t != None: 
            n = ListNode(t.val)
            n.next = back
            back = n
            t = t.next

        forw = head
        while forw != None:
            if forw.val != back.val: return False
            forw = forw.next
            back = back.next
        
        return True