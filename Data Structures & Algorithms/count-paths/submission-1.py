class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = []
        for i in range(m):
            res.append([0] * n)
        for k in range(n):
            res[0][k] = 1
        for k in range(m):
            res[k][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]