class Solution:
    def isValid(self, s: str) -> bool:
        open_para = ['(', '{', '[']
        close_para = [')', '}', ']']
        mp = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in open_para:
                stack.append(c)
            elif c in close_para:
                if not stack:
                    return False
                para = stack.pop()
                if para != mp[c]:
                    return False

        if not stack:
            return True
        return False
