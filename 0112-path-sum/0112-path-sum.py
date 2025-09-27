# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        if root == None: return False

        from collections import deque

        q = deque()

        q.append([root, root.val])

        while q:
            rt, total = q.popleft()

            if rt.left == None and rt.right == None:
                if total == targetSum: return True
            if rt.left:
                q.append([rt.left, total + rt.left.val])
            if rt.right:
                q.append([rt.right, total + rt.right.val])

        return False