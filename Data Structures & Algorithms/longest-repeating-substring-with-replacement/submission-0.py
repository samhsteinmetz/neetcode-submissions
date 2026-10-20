class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # sliding window with hash map 
        # length of hash map 

        count = {}

        get = count.get
        l = 0
        maxF = 0

        maxSize = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                #increment left side until good
                count[s[l]] -=1
                l+=1
            maxSize = max(maxSize, r-l+1)
            
        return maxSize
