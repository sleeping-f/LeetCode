# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums, l = None, r = None, root = None):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if l == None: 
            l = 0
            r = len(nums) - 1
        print(l, r, root)
        if l < 0 or l > r: return None

        mid = (r+l) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums, l, mid-1, root.left)
        root.right = self.sortedArrayToBST(nums, mid+1, r, root.right)

        return root
        
            
        