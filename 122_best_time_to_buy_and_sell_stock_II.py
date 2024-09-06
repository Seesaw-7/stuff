class Solution:
    # O(n) time, O(1) space
    def maxProfit1(self, prices: list[int]) -> int:
        profits = 0
        if len(prices) == 0:
            return profits

        buy_flag = 0 # whether currently holding a share
        buy = prices[0]
        
        for i in range(0, len(prices)-1):
            if prices[i] > buy and buy_flag:
                profits += prices[i] - buy
                buy_flag = 0
            if prices[i+1] > prices[i]:
                buy = prices[i]
                buy_flag = 1
        
        if prices[-1] > buy and buy_flag:
            profits += prices[-1] - buy

        return profits

    # simplified
    def maxProfit(self, prices: list[int]) -> int:
        profits = 0
        start = prices[0]

        for price in prices:
            if price > start:
                profits += price - start
            start = price

        return profits
