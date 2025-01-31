class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_idx = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in val_idx:
                return [val_idx[target-nums[i]], i]
            val_idx[nums[i]] = i


"""First Solution: time o(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
"""