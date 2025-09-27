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
        '''
        if root == None: return 0
        flag = False
        def BFSmin(root, count = 1, minDep = float('inf')):
            if flag == True:

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
                '''
        if root == None: return 0
        from collections import deque

        q = deque()

        count = 1
        q.append([root, count])
        while q:
            froot = q.popleft()
            count = froot[1]
            if froot[0].left == None and froot[0].right == None:
                return count
            elif froot[0].left == None:
                q.append([froot[0].right, count+1])
            elif froot[0].right == None:
                q.append([froot[0].left, count+1])
            else:
                q.append([froot[0].left, count+1])
                q.append([froot[0].right, count+1])

          

            

            

    
        return(BFSmin(q))