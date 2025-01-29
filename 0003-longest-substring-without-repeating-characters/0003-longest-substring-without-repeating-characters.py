class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
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
            