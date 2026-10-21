class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # smallStringLength = len(t)
        # if smallStringLength > len(s):
        #     return ''
        # r = len(t)
        # currSS = set(s[0:r])
        # for l in range(len(s)):
        #     currSS = s[l:r]
        #     for char in t:
        #         if char not in

        # s big
        # t small

        if t == '':
            return ''
        countT = {}
        window = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float('infinity')

        l = 0
        for r in range(len(s)):
            curr = s[r]
            window[curr] = 1 + window.get(curr, 0)

            if curr in countT and window[curr] == countT[curr]:
                have+=1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l, r = res
        if resLen == float("infinity"):
            return ''
        return s[l: r + 1]
            




