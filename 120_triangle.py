class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        depth = len(triangle)
        dp = [[float('inf') for _ in range(depth+1)] for _ in range(depth+1)]

        def helper(i:int, idx:int) -> int:
            if i == depth:
                return 0
            if dp[i+1][idx] == float('inf'):
                dp[i+1][idx] = helper(i+1, idx)
            if  dp[i+1][idx+1] == float('inf'):
                dp[i+1][idx+1] = helper(i+1, idx+1)
            
            print(dp)
            return triangle[i][idx] + min(dp[i+1][idx], dp[i+1][idx+1])

        return helper(0, 0)