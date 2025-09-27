# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None: return 0
        def BFSmin(root, count = 1, minDep = float('inf')):
            if root.left == None and root.right == None:
                minDep = min(count, minDep)
                return minDep
            elif root.left == None:
                return(BFSmin(root.right, count+1, minDep))
            elif root.right == None:
                return(BFSmin(root.left, count+1, minDep))
            else:
                n = BFSmin(root.left, count+1, minDep)
                m = BFSmin(root.right, count+1, minDep)
                return min(n, m)

            

            

    
        return(BFSmin(root))