class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(val):
            if val >= len(nums):
                if sum(curr) == target:
                    res.append(curr.copy())
                return
            elif sum(curr) == target:
                res.append(curr.copy())
                return
            elif sum(curr) > target:
                return
            curr.append(nums[val])
            dfs(val)
            curr.pop()
            dfs(val + 1)
        dfs(0)
        return res