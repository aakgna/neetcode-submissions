class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []

        def dfs(i):
            s = sum(curr)
            if s == target:
                res.append(curr.copy())
                return
            elif s > target:
                return
            elif i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i)

            curr.pop()
            dfs(i+1)
        dfs(0)
        return res