class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, x+1):
            num = i * i
            if num == x:
                return i
            if num > x:
                return i-1

    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        temp = x // 2
        while temp * temp > x:
            temp = temp // 2

        for i in range(temp, (temp+1) * 2):

            sqr = i * i
            if sqr == x:
                return i
            elif sqr > x:
                return i-1

    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        start = 0
        end = x

        while True:
            if start == end or start == end - 1:
                return start
            mid = (start + end) // 2
            sqr = mid * mid
            if sqr == x:
                return mid
            if sqr < x:
                start = mid
            if sqr > x:
                end = mid