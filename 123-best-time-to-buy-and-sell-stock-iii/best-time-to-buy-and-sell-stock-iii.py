class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def max_profit_with_index(prices):
            min_price = float('inf') 
            max_profit = 0  
            min_index = 0  
            buy_index = 0 
            sell_index = 0 

            for i, price in enumerate(prices):
                if price < min_price:
                    min_price = price  
                    min_index = i 

                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit  
                    buy_index = min_index
                    sell_index = i 

            return max_profit, buy_index, sell_index

        profit, buy, sell = max_profit_with_index(prices)

        possible1, _, _ = max_profit_with_index(prices[:buy])
        possible2, _, _ = max_profit_with_index(prices[sell + 1:])
        possible3, _, _ = max_profit_with_index(reversed(prices[buy:sell]))

        return profit + max(possible1, possible2, possible3)