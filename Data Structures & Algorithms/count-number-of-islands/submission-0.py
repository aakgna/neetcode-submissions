class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        def mark(idx):
            if idx[0] < 0 or idx[0] >= len(grid) or idx[1] < 0 or idx[1] >= len(grid[0]):
                return
            val = str(idx[0]) + str(idx[1])
            if grid[idx[0]][idx[1]] == "0" or val in visited:
                return
            visited.add(str(idx[0]) + str(idx[1]))
            mark([idx[0] + 1, idx[1]])
            mark([idx[0] - 1, idx[1]])
            mark([idx[0], idx[1] + 1])
            mark([idx[0], idx[1] - 1])
            return
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if str(i) + str(j) not in visited and grid[i][j] == "1":
                    mark([i, j])
                    res += 1
        return res