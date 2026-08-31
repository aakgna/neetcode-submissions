# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.listp = list()
        self.listq = list()
        self.dfs(p, self.listp)
        self.dfs(q, self.listq)
        return self.listp == self.listq
    def dfs(self, root, order):
        if root == None:
            order.append(None)
            return
        self.dfs(root.left, order)
        self.dfs(root.right, order)
        order.append(root.val)
        return