class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxMin = float('inf')

        maxMax = float('-inf')
        for p in prices:
            maxMin = min(maxMin, p)
            maxMax = max(maxMax, p - maxMin)

        return maxMax

