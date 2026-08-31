# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = k
        res = None
        def dfs(r):
            nonlocal smallest, res
            if r == None:
                return
            dfs(r.left)
            smallest -= 1
            if smallest == 0:
                res = r.val
            dfs(r.right)
        dfs(root)
        return res
            