class Solution:
    def isPalindrome1(self, s: str) -> bool:
        len_s = len(s)
        l = 0 # left
        r = len_s - 1 # right
        alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        while l < r:
            while s[l] not in alphanumeric and l < len(s) - 1:
                l += 1
            while s[r] not in alphanumeric and r > 0:
                r -= 1
            if l < r and not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True

    def isPalindrome(self, s: str) -> bool:
        len_s = len(s)
        l = 0 # left
        r = len_s - 1 # right

        while l < r:
            while not s[l].isalnum() and l < len_s - 1:
                l += 1
            while not s[r].isalnum() and r > 0:
                r -= 1
            if l < r and not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
