# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def swap(root):
            if root == None : return
            elif root.left == None and root.right == None: return
            elif root.left == None:
                root.left = root.right
                root.right = None
            elif root.right == None:
                root.right = root.left
                root.left = None
                #print(root)

            else:
                n = root.left
                root.left = root.right
                root.right = n

            #print(root)

            swap(root.left)
            swap(root.right)
        swap(root)

        return root
        