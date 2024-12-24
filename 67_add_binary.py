class Solution:
    # 16 mins
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carrier = 0
        i = len(a) - 1
        j = len(b) - 1
        while carrier or i >= 0  or j >= 0:
            print(i, j, carrier)
            if i < 0 and j < 0:
                ans.append('1')
                carrier = 0
            elif i < 0:
                num = carrier + int(b[j]) 
                if num == 2:
                    num -= 2
                    carrier = 1
                else:
                    carrier = 0
                ans.append(str(num))
                j -= 1
            elif j < 0:
                num = carrier + int(a[i]) 
                if num == 2:
                    carrier = 1
                    num -= 2
                else:
                    carrier = 0
                ans.append(str(num))
                i -= 1
            else:
                num = carrier + int(a[i]) + int(b[j])
                if num == 3:
                    carrier = 1
                    num -= 2
                elif num == 2:
                    carrier = 1
                    num -= 2
                else:
                    carrier = 0
                ans.append(str(num))
                i -= 1
                j -= 1

        ans.reverse()
        ans = ''.join(ans)
        return ans

    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        ans = []
        carrier = 0
        while a or b or carrier:
            summ = carrier
            if a:
                summ += int(a.pop())
            if b:
                summ += int(b.pop())
            if summ >= 2:
                carrier = 1
                summ -= 2
            else:
                carrier = 0
            ans.append(str(summ))
        ans.reverse()
        return ''.join(ans)

    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        ans = []
        carrier = 0
        while a or b or carrier:
            summ = carrier
            if a:
                summ += int(a.pop())
            if b:
                summ += int(b.pop())
            if summ >= 2:
                carrier = 1
                summ -= 2
            else:
                carrier = 0
            ans.append(str(summ))
        ans.reverse()
        return ''.join(ans)
    