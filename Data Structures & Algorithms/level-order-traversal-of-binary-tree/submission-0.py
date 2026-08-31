# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        queue = list()
        queue.append(root)
        while queue:
            ans = []
            curr_q = list()
            for r in queue:
                ans.append(r.val)
                if r.left:
                    curr_q.append(r.left)
                if r.right:
                    curr_q.append(r.right)
            res.append(ans)
            queue = curr_q
        return res