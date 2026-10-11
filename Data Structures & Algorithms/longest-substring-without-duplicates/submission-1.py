class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        length = len(s)
        maxLen = 0
        
        while left<length:
            curr = s[left:right]
            if right<length and s[right] not in curr:
                right+=1
            else:
                left+=1
                maxLen = max(maxLen, len(curr))

        return maxLen
                
