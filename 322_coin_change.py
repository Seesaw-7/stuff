from functools import cache

class Solution:
    def coinChange1(self, coins: list[int], amount: int) -> int:
        
        @cache
        def helper(amount: int) -> int:
            temp = [amount-x for x in coins if amount-x>=0]
            if 0 in temp:
                return 1
            if not temp:
                return -1
            res = map(helper, temp)
            res = [x for x in res if x != -1]
            if not res:
                return -1
            return min(res) + 1

        if amount == 0:
            return 0
        return helper(amount)

    def coinChange2(self, coins: list[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            if dp[i] == amount+1: # early termination
                continue
            for c in coins:
                if i+c <= amount:
                    dp[i+c] = min(dp[i+c], dp[i]+1)

        return -1 if dp[amount] == amount+1 else dp[amount]

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [amount+1 for _ in range(amount)]

        for i in range(amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)

        return -1 if dp[amount] == amount+1 else dp[amount]
