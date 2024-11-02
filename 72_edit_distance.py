class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[i]+[-1 for _ in range(m)] for i in range(n+1)]
        dp[0] = [i for i in range(m+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                rep = 0 if word2[i-1] == word1[j-1] else 1
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] +rep)

        return dp[-1][-1]