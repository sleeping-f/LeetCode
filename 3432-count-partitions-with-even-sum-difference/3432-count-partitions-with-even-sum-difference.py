class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(n-1):
            left = 0
            for l in range(i+1):
                left += nums[l]
            right = 0
            for r in range(i+1, n):
                right += nums[r]
            if (left - right) % 2 == 0: ans += 1

        return ans