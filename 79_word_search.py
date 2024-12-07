class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        len_word = len(word)
        
        def helper(i:int, j:int, path:set((int,int))) -> bool:
            len_path = len(path)
            if len_path == len_word:
                return True
            if board[i][j] != word[len_path]:
                return False
            new_path = path.copy()
            new_path.add((i,j))
            if len_path + 1 == len_word:
                return True
            a, b, c, d = False, False, False, False
            if i != 0 and (i-1,j) not in path:
                a = helper(i-1, j, new_path)
            if i != n-1 and (i+1, j) not in path:
                b = helper(i+1, j, new_path)
            if j != 0 and (i, j-1) not in path:
                c = helper(i, j-1, new_path)
            if j != m-1 and (i, j+1) not in path:
                d = helper(i, j+1, new_path)
            return a or b or c or d

        for i in range(n):
            for j in range(m):
                if helper(i, j, set()):
                    return True
        return False
    
    # another coding style:
    # https://leetcode.com/problems/word-search/solutions/27660/python-dfs-solution-with-comments/?envType=study-plan-v2&envId=top-interview-150
    def exist(self, board, word):
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res