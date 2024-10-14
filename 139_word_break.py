from functools import cache

class Solution:
    # use backtracking with cache
    # tuple(wordDict) because cache store one series of function inputs as a key of a dict
    def wordBreak1(self, s: str, wordDict: list[str]) -> bool:
        @cache
        def helper(s: str, wordDict) -> bool:
            valid = []
            for w in wordDict:
                if s.find(w) == 0:
                    valid.append(w)
            while valid:
                w = valid.pop()
                if len(w) == len(s):
                    return True
                if helper(s[len(w):], wordDict):
                    return True
            return False

        return helper(s, tuple(wordDict))

    # dp without @cache, but functionally equal
    def wordBreak2(self, s: str, wordDict: list[str]) -> bool:
        dp = [1 for _ in range(len(s))]

        def helper(s: str, wordDict) -> bool:
            len_s = len(s)
            valid = []
            for w in wordDict:
                if s.find(w) == 0:
                    valid.append(w)
            while valid:
                w = valid.pop()
                len_w = len(w)
                if len_w == len_s:
                    return True
                new_s = s[len_w:]
                if not dp[-len(new_s)]:
                    continue
                if helper(new_s, wordDict):
                    return True
                else:
                    dp[-len(new_s)] = 0
            return False  

        return helper(s, tuple(wordDict))

    # Traditional DP
    # dp[i] is set to true if a valid word (word sequence) ends there
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if i > 0:
                if dp[i-1] == 0:
                    continue
            for w in wordDict:
                if s[i:].find(w) == 0:
                    dp[i+len(w)-1] = 1
        return dp[-1]
