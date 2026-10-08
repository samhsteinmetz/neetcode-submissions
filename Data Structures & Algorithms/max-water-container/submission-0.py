class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        ret = -1
        while r>l:
            area = (r-l) * min(heights[r], heights[l])
            ret = max(ret, area)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return ret