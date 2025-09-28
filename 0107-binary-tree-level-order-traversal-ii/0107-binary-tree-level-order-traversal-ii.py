# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None: return []

        q = deque()
        q.append(root)
        lvl_ord = []
        lvl = 0

        while q:
            lvl_ord.append([])
            lvl_len = len(q)

            for _ in range(lvl_len):
                item = q.popleft()
                lvl_ord[lvl].append(item.val)

                if item.left: q.append(item.left)
                if item.right: q.append(item.right)

            lvl += 1

        lvl_ord.reverse()
        return lvl_ord

        