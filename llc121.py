class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') #this is an idea to set minimum to infinity so everything is smaller to start
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            curr_profit = price - min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit        