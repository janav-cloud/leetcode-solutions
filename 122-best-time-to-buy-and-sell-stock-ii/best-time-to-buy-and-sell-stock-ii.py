class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for x in range(1, len(prices)):
            if prices[x] - prices[x - 1] > 0:
                profit += prices[x] - prices[x - 1]

        return profit