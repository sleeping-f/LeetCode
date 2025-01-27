class Solution(object):
    def minimumRecolors(self, blocks, k):
        def blackit(arr, t, k, s = 0):
            arr = arr[0:t] + "B" + arr[t+1:]
            #print(arr, t, k)
            s += 1
            ans = None
            if checkit(arr, k) == True: 
                return s
            else:
                for i in range(t+1, len(blocks)):
                    if arr[i] == "W":
                        ans = blackit(arr, i, k, s)
                        break
            return ans
            

        def checkit(arr, k):
            for i in range(len(arr)):
                if arr[i] == 'B':
                    count = 1
                    if k == count: return True
                    for j in range(i+1, len(arr)):
                        if arr[j] == "B": count += 1
                        else: break
                        if count == k: 
                            return True
            return False
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        steps = None
        if checkit(blocks, k): return 0
        for col in range(len(blocks)):
            if blocks[col] == "W":
                ns = blackit(blocks, col, k)
                if ns != None:
                    if steps == None: steps = ns
                    elif ns < steps: steps = ns
        return steps

        

        