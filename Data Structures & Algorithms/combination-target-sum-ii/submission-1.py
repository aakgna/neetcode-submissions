class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []
        visited = set()
        candidates.sort()
        def dfs(i):
            if i >= len(candidates):
                if sum(subsets) == target and tuple(subsets) not in visited:
                    v = subsets.copy()
                    res.append(v)
                    visited.add(tuple(v))
                return
            subsets.append(candidates[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return res