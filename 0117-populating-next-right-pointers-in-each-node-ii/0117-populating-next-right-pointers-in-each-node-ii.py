 
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return None

        q = deque()
        q.append(root)

        while q:
            lvl = []

            for _ in range(len(q)):
                node = q.popleft()
                lvl.append(node)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            items = len(lvl)
            for i in range(items):
                if i == items-1:
                    lvl[i].next = None
                else:
                    lvl[i].next = lvl[i+1]
        return root
        