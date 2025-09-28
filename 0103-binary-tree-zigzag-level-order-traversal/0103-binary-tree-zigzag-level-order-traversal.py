# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        lvl_ord = []
        lvl = 0

        if root == None: return []

        q = deque()
        q.append(root)

        while q:
            lvl_items = len(q)
            lvl_ord.append([])

            for _ in range(lvl_items):
                item = q.popleft()
                lvl_ord[lvl].append(item.val)

                if item.left: q.append(item.left)
                if item.right: q.append(item.right)
            if lvl % 2 != 0:
                lvl_ord[lvl].reverse()
            lvl += 1

        return lvl_ord