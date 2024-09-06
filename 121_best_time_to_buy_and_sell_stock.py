class Solution: 
    # accepted O(nlogn)
    def maxProfit1(self, prices: list[int]) -> int:

        def helper(l: list[int]) -> int:
            if len(l) == 1 or len(l) == 0:
                return 0
            else:
                min_value = min(l)
                min_idx = l.index(min_value)
                print(min_idx)
                if min_idx+1 < len(l) :
                    max_profit_right = max(l[min_idx+1:]) - min_value
                else:
                    max_profit_right = 0
                max_profit_left = helper(l[:min_idx])
                max_profit = max(max_profit_left, max_profit_right)
                return max_profit

        return helper(prices)

    # accepted O(n)
    def maxProfit(self, prices: list[int]) -> int:
        min_value = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_value:
                min_value = price
            else:
                if price - min_value > max_profit:
                    max_profit = price - min_value

        return max_profit
