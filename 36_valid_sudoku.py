class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_valid_row(board)
                and self.is_valid_col(board)
                and self.is_valid_grid(board))

    @staticmethod
    def is_valid_row1(board):
        for i in board:
            cnt = {}
            for j in i:
                if j != ".":
                    if j in cnt:
                        return False
                    cnt[j] = 1
        return True

    @staticmethod  
    def is_valid_col1(board):
        # cnts = [{}] * 9 which will create 9 mutable dicts, which will always be the same
        # despite that we only one to change one of them
        cnts = [{} for _ in range(9)]
        for i,line in enumerate(board):
            for j,num in enumerate(line):
                if num != ".":
                    if num in cnts[j]:
                        return False
                    cnts[j][num] = 1
        return True

    @staticmethod
    def is_valid_grid1(board):
        cnts = [set() for _ in range(9)]
        for i, line in enumerate(board):
            for j, num in enumerate(line):
                k = 0
                if i <= 2:
                    if j <= 2:
                        k = 0
                    elif 2 < j <= 5:
                        k = 1
                    else:
                        k = 2
                elif 2 < i <= 5:
                    if j <= 2:
                        k = 3
                    elif 2 < j <= 5:
                        k = 4
                    else:
                        k = 5
                else:
                    if j <= 2:
                        k = 6
                    elif 2 < j <= 5:
                        k = 7
                    else:
                        k = 8
                if num != ".":
                    if num in cnts[k]:
                        return False
                    cnts[k].add(num)
        return True

    # better python coding style
    @staticmethod
    def is_valid_unit(l: List[str]):
        l = [x for x in l if x != "."]
        return len(l) == len(set(l))

    def is_valid_row(self, board):
        for i in board:
            if not self.is_valid_unit(i):
                return False
        return True

    def is_valid_col(self, board):
        for i in zip(*board):
            if not self.is_valid_unit(i):
                return False
        return True

    def is_valid_grid(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                l = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid_unit(l):
                    return False
        return True
