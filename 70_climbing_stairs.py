class Solution:
    # iterative dp
    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

    # recursive dp beats 91%
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        def helper(n: int) -> int:
            if dp[n-1]:
                return dp[n-1]
            dp[n-1] = helper(n-1) + helper(n-2)
            return dp[n-1]

        return helper(n)
        