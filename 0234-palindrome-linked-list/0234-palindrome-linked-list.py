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
        self.cur = head
        return self.recPalin(head)
    
    def recPalin(self, head):
        if head == None: return True

        test = self.recPalin(head.next) and head.val == self.cur.val
        self.cur = self.cur.next
        return test
        """
        First Solve
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
        """