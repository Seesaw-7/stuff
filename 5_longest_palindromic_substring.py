class Solution:
    # May, 2024, brute force
    @staticmethod
    def check(s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return s

        dom = list(range(1,(len(s)+1)))
        dom.reverse()

        for i in dom:
            for j in range(len(s) - i + 1):
                if self.check(s[j:j+i]):
                    return s[j:j+i]
        return s

        
    # brute force, time limit
    def longestPalindrome(self, s: str) -> str:

        def if_pal(s: str) -> bool:
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        len_s = len(s)
        
        max_len = 0
        max_sen = ''
        for i in range(len_s):
            for j in range(1, len_s+1):
                if if_pal(s[i:j]):
                    if j - i > max_len:
                        max_len = j - i
                        max_sen = s[i:j]

        return max_sen

    # a trick by iterating along, and find the longest palindrome at centre
    # expanding around centre
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_sen = ''
        for i in range(len(s)):
            cnt = 1
            while i - cnt >= 0 and i + cnt < len(s):
                if s[i-cnt] != s[i+cnt]:
                    break
                cnt += 1
            if 2*cnt - 1 > max_len:
                max_len = 2*cnt-1
                max_sen = s[i-cnt+1:i+cnt]
            cnt = 0
            while i - cnt-1 >= 0 and i + cnt < len(s):
                if s[i-cnt-1] != s[i+cnt]:
                    break
                cnt += 1
            if 2*cnt > max_len:
                max_len = 2*cnt
                max_sen = s[i-cnt:i+cnt]

        return max_sen

    # recursive, but memory limit
    @staticmethod
    def if_pal(s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True     

    @cache
    def longestPalindrome(self, s: str) -> str:
        if self.if_pal(s):
            return s
        
        s1 = self.longestPalindrome(s[1:])
        s2 = self.longestPalindrome(s[:-1])
        return s1 if len(s1) > len(s2) else s2

    # dp[i][j] denotes that a string is valid starting from i and ending in j
    # They will occupy the top right half of the matrix
    # This uses the same idea as expanding around the centre, and the same time complexity
    # dp[i][j] is valid if s[i] == s[j] and dp[i+1][j-1] is valid
    # so iterating bottom-up(outer) and left-right(inner)
    # The starting points are that dp[x][x] should be True for all x
    # 
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s < 1:
            return s

        max_len = 1
        max_str = s[0]
        dp = [[False for _ in range(len_s)] for _ in range(len_s)] # Is boolean more space efficient than int? I think so.. So, use True/False instead of 0/1
        for i in reversed(range(len_s)): # 
            dp[i][i] = True
            for j in reversed(range(i+1, len_s)):
                if s[i] == s[j] and (j == i + 1 or dp[i+1][j-1]): # the centre is (the centre of two chars) or (one char)
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i
                        max_str = s[i:j+1]

        return max_str
 