class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subs = ''
        max = 0
        count = 0
        for ch in s:
            if not ch in subs:
                subs += ch
                count += 1
            else:
                subs = ch
                if count > max: max = count
                count = 1
        if count > max: max = count

        return max
            