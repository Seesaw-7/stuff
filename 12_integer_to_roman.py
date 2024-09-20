class Solution:
    def intToRoman(self, num: int) -> str:
        rom = ""

        int2rom = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        vals = [1000, 500, 100, 50, 10, 5, 1]

        for i, val in enumerate(vals):
            n = num // val
            if i < len(vals) - 1:
                m = num // vals[i+1]

            if n == 4 and i != 0:
                rom += int2rom[val] + int2rom[vals[i-1]]
                num = num % val
            elif i < len(vals) -1 and i > 0 and m == 9:
                rom += int2rom[vals[i+1]] + int2rom[vals[i-1]]
                num = num - vals[i-1] + vals[i+1]
            else:
                rom += int2rom[val] * n
                num = num % val

        return rom
