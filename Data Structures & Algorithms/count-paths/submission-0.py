class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    matrix[row][col] = 1
                else:
                    matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
        return matrix[m-1][n-1]