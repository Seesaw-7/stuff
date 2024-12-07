class Solution:
    def count25(self, n:int) -> int:
        num5 = 0

        while n % 5 == 0 and n >= 5:
            n = n // 5
            num5 += 1

        return num5

    def trailingZeroes(self, n: int) -> int:
        num5 = 0
        for i in range(1, n+1):
            num5 += self.count25(i)
        return num5
