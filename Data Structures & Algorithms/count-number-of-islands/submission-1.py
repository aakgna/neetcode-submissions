class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def mark(root):
            if 0 <= root[0] < len(grid) and 0 <= root[1] < len(grid[0]):
                print(visited)
                if grid[root[0]][root[1]] == "0" or tuple(root) in visited:
                    return
                visited.add(tuple(root))
                
                mark([root[0] + 1, root[1]])
                mark([root[0] - 1, root[1]])
                mark([root[0], root[1] + 1])
                mark([root[0], root[1] - 1])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    mark([i,j])
        return res
