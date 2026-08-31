class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(val):
            if val >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[val])
            dfs(val + 1)
            curr.pop()
            dfs(val + 1)
        dfs(0)
        return res