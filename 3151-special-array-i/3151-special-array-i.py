class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            if len(nums) == 1: return True
            if (nums[i] % 2 == 0 and nums[i+1] % 2 == 0)  or (nums[i] % 2 == 1 and nums[i+1] % 2 == 1): return False
        return True
        