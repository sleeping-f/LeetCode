# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def sym(p, q):
            if p == None and q == None: return True
            if p == None and q != None: return False
            if p != None and q == None: return False
            if p.val != q.val: return False

            return sym(p.left, q.right) and sym(p.right, q.left)

        return sym(root.left, root.right)