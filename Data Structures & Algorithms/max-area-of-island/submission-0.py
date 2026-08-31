class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def counting(root):
            if not (0 <= root[0] < len(grid) and 0 <= root[1] < len(grid[0])):
                return 0
            if grid[root[0]][root[1]] == -1 or grid[root[0]][root[1]] == 0:
                return 0
            grid[root[0]][root[1]] = -1

            val1 = counting([root[0] + 1, root[1]])
            val2 = counting([root[0] - 1, root[1]])
            val3 = counting([root[0], root[1] + 1])
            val4 = counting([root[0], root[1] - 1])

            return val1 + val2 + val3 + val4 + 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, counting([i,j]))
        return res