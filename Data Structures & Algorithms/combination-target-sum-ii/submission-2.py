class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        seen = set()
        candidates.sort()
        def dfs(i):
            if i >= len(candidates):
                if sum(curr) == target and tuple(curr) not in seen:
                    res.append(curr.copy())
                    seen.add(tuple(curr.copy()))
                return
            elif sum(curr) == target and tuple(curr) not in seen:
                res.append(curr.copy())
                seen.add(tuple(curr.copy()))
            elif sum(curr) > target:
                return
            elif tuple(curr) in seen:
                return

            curr.append(candidates[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)
        dfs(0)
        return res