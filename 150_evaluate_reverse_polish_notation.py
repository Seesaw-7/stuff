class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        for t in tokens:
            if t.isdigit():
                num_stack.append(int(t))
            elif len(t) > 1 and t[0] == '-':
                num_stack.append(int(t))
            else:
                a = num_stack.pop()
                b = num_stack.pop()
                if t == '+':
                    num_stack.append(a + b)
                elif t == '-':
                    num_stack.append(b - a)
                elif t == '*':
                    num_stack.append(b * a)
                elif t == '/':
                    num_stack.append(int(b / a))
        return num_stack[-1]
