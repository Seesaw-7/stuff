class Solution:
    def isHappy1(self, n: int) -> bool:
        loop = set()

        accum = 0
        num = n
        while True:
            accum = 0
            while num > 0:
                accum += (num % 10) ** 2
                num = num // 10
            if accum == 1:
                return True
            else: 
                if accum in loop:
                    return False
                loop.add(accum)
                num = accum

    # parallel calc
    def isHappy(self, n: int) -> bool:
        loop = set()

        while n != 1:
            n = sum([int(x) ** 2 for x in str(n)])
            if n in loop:
                return False
            loop.add(n)
        
        return True