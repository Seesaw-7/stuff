class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp_live = []
        temp_die = []
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                live_nbs = [board[x][y] for x in range(i-1,i+2) if 0 <= x < m for y in range(j-1, j+2) if 0 <= y < n and board[x][y] == 1 and (x != i or y != j)]
                num = len(live_nbs)
                if board[i][j] == 1:
                    if num < 2 or num > 3:
                        temp_die.append((i, j))
                else:
                    if num == 3:
                        temp_live.append((i, j))

        for i, j in temp_die:
            board[i][j] = 0

        for i,j in temp_live:
            board[i][j] = 1
