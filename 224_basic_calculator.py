class Solution:
    def calculate1(self, s: str) -> int:
        tokens = []

        i  = 0
        while i < len(s):
            if s[i] != ' ':
                if s[i].isdigit():
                    num = []
                    while i < len(s) and s[i].isdigit():
                        num.append(s[i])
                        i += 1
                    num = ''.join(num)
                    tokens.append(int(num))
                else:
                    tokens.append(s[i])
                    i += 1
            else:
                i += 1

        stack = []
        i = 0
        operators = ['+', '-']
        for i,t in enumerate(tokens):
            if t == '(':
                stack.append(t)
            elif isinstance(t, int):
                if len(stack) > 1 and stack[-1] in operators and isinstance(stack[-2], int):
                    o = stack.pop() 
                    a = stack.pop()
                    b = t
                    match o:
                        case '+':
                            stack.append(a + b)
                        case '-':
                            stack.append(a - b)
                else:
                    stack.append(t)
            elif t == '-':
                if not stack or len(stack) > 1 and stack[-1] == '(':
                    stack.append(0)
                stack.append('-')
            elif t == '+':
                stack.append('+')
            elif t == ')':
                val = stack.pop()
                stack.pop()
                while len(stack) > 1 and stack[-1] in operators and isinstance(stack[-2], int):
                    o = stack.pop() 
                    a = stack.pop()
                    match o:
                        case '+':
                            val = a + val
                        case '-':
                            val = a - val      
                stack.append(val) 

        return stack[-1]

    # https://leetcode.com/problems/basic-calculator/solutions/546092/simple-python-solution-using-stack-with-explanation-inline/?envType=study-plan-v2&envId=top-interview-150
    def calculate(self, s: str) -> int:
        """
        1. Take 3 containers:
        num -> to store current num value only
        sign -> to store sign value, initially +1
        res -> to store sum
        When ( comes these containers used for calculate sum of intergers within () brackets.
        --------------------
        2. When c is + or -
        Move num to res, because we need to empty num for next integer value.
        set num = 0
        sign = update with c
        --------------------
        3. When c is '('
        Here, we need num, res, sign to calculate sum of integers within ()
        So, move num and sign to stack => [num, sign]
        Now reset - res = 0, num = 0, sign = 1 (default)
        --------------------
        4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -] 
        res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
        res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
        res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
        --------------------
        Simple Example: 2 - 3
        Initially res will have 2,i.e. res = 2
        then store '-' in sign. it will be used when 3 comes. ie. sign = -1
        Now 3 comes => res = res + num*sign
        Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
        """
        num = 0
        sign = 1
        res = 0
        stack = []
        for c in s: # iterate till last character
            if c.isdigit(): # process if there is digit
                num = num*10 + int(c) # for consecutive digits 98 => 9x10 + 8 = 98
            elif c in '-+': # check for - and +
                res += num*sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res +=sign*num
                res *=stack.pop()
                res +=stack.pop()
                num = 0
        return res + num*sign