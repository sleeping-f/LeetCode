# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root, sum = 0):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root.left and not root.right: return 0
        def sumLeft(root, sum = 0, flag = False):
            if not root: return [0, False]

            elif root.left:
                if not root.left.left and not root.left.right:
                    flag = True
                    sum = root.left.val

            l = sumLeft(root.left)
            r = sumLeft(root.right)

            if flag == True:
                if l[1] == True:
                    sum += l[0]
                if r[1] == True:
                    sum += r[0]
                return [sum, True]
            else:
                if l[1] and r[1]:
                    sum = l[0] + r[0]
                    return [sum, True]
                elif l[1]:
                    sum = l[0]
                    return [sum, True]
                elif r[1]:
                    sum = r[0]
                    return [sum, True]
                else:
                    return [0, False]

        

        return(sumLeft(root)[0])
        