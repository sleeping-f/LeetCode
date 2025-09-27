# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        '''
        level_order = []

        if root == None: return level_order

        #from collections import deque

        q = deque()

        q.append([root, 0])

        while q:
            rt, level = q.popleft()

            if len(level_order) < level+1:
                level_order.append([])
            level_order[level].append(rt.val)

            if rt.left:
                q.append([rt.left, level+1])
            if rt.right:
                q.append([rt.right, level+1])

        return level_order
        '''

        lvl_order = []
        if not root: return []

        q = deque()
        q.append(root) 

        while q:    
            lvl = len(q)
            lvl_list = []

            for _ in range (lvl):
                node = q.popleft()
                lvl_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl_order.append(lvl_list)
        
        return lvl_order


