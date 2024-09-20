class Solution:
    # with built-in
    def lengthOfLastWord1(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
        
    # do not use built-in
    def lengthOfLastWord(self, s: str) -> int:
        flag = 0
        cnt = 0

        for c in reversed(s):
            if c != ' ':
                if not flag:
                    flag = 1
                    cnt = 1
                else:
                    cnt += 1
            else:
                if flag:
                    return cnt

        return cnt
