class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        n = len(xstr)
        for i in range(n // 2):
            if xstr[i] != xstr[~i]:
                return False
        return True