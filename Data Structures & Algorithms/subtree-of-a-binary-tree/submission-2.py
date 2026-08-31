# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.arr_root = list()
        self.arr_sub = list()
        
        self.dfs(root, self.arr_root)
        self.dfs(subRoot, self.arr_sub)
        if self.arr_root == self.arr_sub:
            return True
        for i in range(0, len(self.arr_root)-len(self.arr_sub)):
            if self.arr_root[i:i+len(self.arr_sub)] == self.arr_sub:
                return True
        return False
    def dfs(self, r, arr):
        if r == None:
            arr.append(None)
            return
        self.dfs(r.left, arr)
        self.dfs(r.right, arr)
        arr.append(r.val)
        return