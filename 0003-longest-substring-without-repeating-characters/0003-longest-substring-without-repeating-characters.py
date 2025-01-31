class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r, ans = 0, 0, 0
        ls = len(s)
        window = ''

        while r < ls:
            while  r < ls and (not s[r] in window):
                window += s[r]
                r += 1
            ans = max(ans, r - l)

            while  r < ls and s[l] != s[r] and l < r:
                l += 1
                window = window[1:]
            window = window[1:]
            l += 1
            print('3- ', window)

        return ans 


""" First Solve: time o(n^2)
        max = 0
        for r in range(len(s)):
            subs = s[r]
            count = 1
            for i in range(r+1, len(s)):
                if not s[i] in subs:
                    subs += s[i]
                    count += 1
                else:
                    break
            if max < count: max = count

        return max
            """