class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        if x < 0: return False
        if x < 10: return True

        l = 0
        mid = 0
        sol = 0

        t = x
        while t > 0:
            l += 1
            t = t // 10
        mid = l // 2

        for i in range(mid):
            sol = sol * 10 + x % 10
            x = x // 10

        if l % 2 != 0: x = x // 10


        if x == sol: return True
        else:
            return False
        

