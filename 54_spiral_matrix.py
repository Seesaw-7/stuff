class Solution:
    def spiralOrder1(self, matrix: list[list[int]]) -> list[int]:
        i = len(matrix[0])
        j = len(matrix) - 1
        num = i  * (j + 1)
        k, l = i - 1, j - 1
        ans = []
        x, y = 0, -1

        while i > 0 or j > 0 or k > 0 or l > 0:
            if num == len(ans):
                return ans
            for _ in range(i):
                y += 1
                ans.append(matrix[x][y])
            i -= 2

            if num == len(ans):
                return ans
            for _ in range(j):
                x += 1
                ans.append(matrix[x][y])
            j -= 2

            if num == len(ans):
                return ans
            for _ in range(k):
                y -= 1
                ans.append(matrix[x][y])
            k -= 2

            if num == len(ans):
                return ans
            for _ in range(l):
                x -= 1
                ans.append(matrix[x][y])
            l -= 2

        return ans

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return matrix and list(matrix.pop(0)) + self.spiralOrder(matrix=[*zip(*matrix)][::-1])
        # using [*matrix.pop(0)] instead of matrix.pop(0) 
        # because zip(*matrix) will create tuples and matrix.pop(0) will thus be a tuple
        # using [*matrix.pop(0)] instead of list(matrix.pop(0)) may be more pythonic?