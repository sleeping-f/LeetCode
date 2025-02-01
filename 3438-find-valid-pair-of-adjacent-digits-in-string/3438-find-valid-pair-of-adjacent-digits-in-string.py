class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        val_n = {}
        serial = ''
        
        for i in range(len(s)):
            if s[i] in val_n:
                val_n[s[i]] += 1
            else:
                val_n[s[i]] = 1
                serial += s[i]


        for i in range(len(s)-1):
            window = s[i] + s[i+1]
            if val_n[window[0]] == int(window[0]) and val_n[window[1]] == int(window[1]) and window[0] != window[1]:
                return window
        return ""
'''
        count = 0
        sol = ''
        for key in serial:
            if val_n[key] == int(key):
                sol += str(key)
                count += 1
            if count == 2:
                break

        if count < 2: return ""
        if sol not in s: 
          sol = sol[1] + sol[0]
          if sol not in s:
            return ""
        return sol


        
        sol = []
        value_count = [0] * 11
        serial = []

        for i in range(len(s)):
            value_count[int(s[i])] += 1

            if value_count[int(s[i])] == int(s[i]):
                sol += s[i]
            if s[i] in sol:
                if value_count[int(s[i])] != int(s[i]):
                    nsol = ''
                    for ch in sol:
                        if ch != s[i]:
                            nsol += ch
                    sol = nsol

        if len(sol) < 2: return ''
        else: 
            for i in range(len[s]):
                if value_count[s[i]] == s[i]:
                    '''