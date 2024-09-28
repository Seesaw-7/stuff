class Solution:
    # 35 min, push single char to stack
    def simplifyPath1(self, path: str) -> str:
        ans = []
        for c in path:
            if c == '/':
                if len(ans) > 3 and ans[-1] == '.' and ans[-2] == '.' and ans[-3] != '/': # meaning previous is a file name
                    ans.append('/')
                elif len(ans) > 2 and ans[-1] == '.' and ans[-2] == '.': # need to back to prev layer
                    ans.pop() #pop .
                    ans.pop() # pop .
                    if len(ans) > 1:
                        ans.pop() # pop /
                        while ans and ans[-1] != '/':
                            ans.pop()
                elif len(ans) > 1 and ans[-1] == '.' and ans[-2] == '/': 
                    ans.pop()
                elif ans and ans[-1] != '/':
                    ans.append('/')
                elif not ans:
                    ans.append('/')
            else:
                ans.append(c)

        if len(ans) >= 3 and ans[-1] == '.' and ans[-2] =='.' and ans[-3] == '/':
            ans.pop()
            ans.pop()
            if len(ans) > 1:
                ans.pop() # pop /
                while ans and ans[-1] != '/':
                    ans.pop()
        if ans[-1] == '.' and ans[-2] == '/':
            ans.pop()
        if ans[-1] == '/' and len(ans) > 1:
            ans.pop()

        return "".join(ans)

    # 17 min push word to stack
    def simplifyPath2(self, path: str) -> str:
        stack = []
        word = []

        for c in path:
            if c == '/':
                if not word:
                    word = ['/']
                elif word == ['/', '.']:
                    word = ['/']
                elif word == ['/', '.', '.']:
                    if stack:
                        stack.pop()
                    word = ['/']
                elif word != ['/']:
                    stack.append("".join(word))
                    word = ['/']
            else:
                word.append(c)

        if word != ['/', '.'] and word != ['/'] and word != ['/', '.', '.']:
            stack.append("".join(word))
        elif stack and word == ['/', '.', '.']:
            stack.pop()

        if not stack:
            stack = ['/']
     
        return "".join(stack)

    # split by '/' and push word
    def simplifyPath(self, path: str) -> str:
        chars = path.split('/')
        stack = []

        for char in chars:
            if char == "..":
                if stack:
                    stack.pop()
            elif char and char != ".":
                stack.append(char)
        
        return '/' + '/'.join(stack)