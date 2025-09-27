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
        '''
        if root == None: return False

        from collections import deque

        q = deque()

        q.append([root, root.val])

        while q:
            rt, total = q.popleft()

            if rt.left == None and rt.right == None:
                if total == targetSum: return True
            elif rt.left and not rt.right:
                q.append([rt.left, total + rt.left.val])
            elif rt.right and not rt.left:
                q.append([rt.right, total + rt.right.val])
            else:
                q.append([rt.left, total + rt.left.val])
                q.append([rt.right, total + rt.right.val])

        return False
        '''
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
        
        return left_sum or right_sum