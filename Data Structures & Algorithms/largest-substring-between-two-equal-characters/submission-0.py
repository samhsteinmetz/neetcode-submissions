class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idx = {}
        ret = -1
        for i in range(len(s)):
            curr = s[i]
            if curr not in idx:
                idx[curr] = i
            else:
                ret = max(i - idx[curr] - 1, ret)
            
        return ret