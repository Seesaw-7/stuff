class Solution:
    # O(n) space
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        temp = []

        for i, line in enumerate(matrix):
            for j, num in enumerate(line):
                if num == 0:
                    matrix[i] = [0] * n
                    temp.append(j)

        matrix[:] = zip(*matrix)
        for j in temp:
            matrix[j] = [0] * m

        matrix[:] = zip(*matrix)

    # O(1) space approach: store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable col0 for column0. 
    # https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
