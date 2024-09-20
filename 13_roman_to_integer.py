class Solution:
    def romanToInt1(self, s: str) -> int:
        res = 0
        i = 0

        while i < len(s):
            if s[i] == 'M':
                res += 1000
            elif s[i] == 'D':
                res += 500
            elif s[i] == 'C':
                if i < len(s)-1 and (s[i+1] == 'D' or s[i+1] == 'M'):
                    res += 400 if s[i+1] == 'D' else 900
                    i += 1
                else:
                    res += 100
            elif s[i] == 'L':
                res += 50
            elif s[i] == 'X':
                if i < len(s)-1 and (s[i+1] == 'L' or s[i+1] == 'C'):
                    res += 40 if s[i+1] == 'L' else 90
                    i += 1
                else:
                    res += 10
            elif s[i] == 'V':
                res += 5
            else:
                if i < len(s)-1 and (s[i+1] == 'V' or s[i+1] == 'X'):
                    res += 4 if s[i+1] == 'V' else 9
                    i += 1
                else:
                    res += 1
            i += 1

        return res

    # Using dict as Macro, dict can also help to compare the defined value of strings
    def romanToInt(self, s: str) -> int:
        rom2num = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        max_val = 0
        summation = 0

        for c in reversed(s):
            if rom2num[c] < max_val:
                summation -= rom2num[c]
            else:
                max_val = rom2num[c]
                summation += rom2num[c]
        
        return summation
