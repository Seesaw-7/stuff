class Solution:
    def rotate1(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix = [[7,4,1],[8,5,2],[9,6,3]] # cannot work because it's not in-place,
                                            # it reallocates a new piece of memory to matrix
        n = len(matrix[0])
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        m = n // 2
        for l in matrix:
            # l.reverse()
            for i in range(m):
                l[i], l[-i-1] = l[-i-1], l[i]

    # directly assign to a list slice
    def rotate2(self, matrix:list[list[int]]) -> None:
        matrix[:] = [list(x)[::-1] for x in zip(*matrix)]

    # copied from solution https://leetcode.com/problems/rotate-image/solutions/18884/seven-short-solutions-1-to-7-lines/?envType=study-plan-v2&envId=top-interview-150
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])
    # seems that leetcode does not care whether the inner layer is a tuple or a list
