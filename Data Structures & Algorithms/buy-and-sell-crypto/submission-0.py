class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = float('inf')
        print(m)
        maxProfit = 0
        for i in range(len(prices)):
            m = min(m, prices[i])
            maxProfit = max(maxProfit, prices[i] - m)

        return maxProfit