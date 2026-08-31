# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if self.helper(root) == -1:
            return False
        else:
            return True
    def helper(self, r):
        if r == None:
            return 0
        val_left = self.helper(r.left)
        val_right = self.helper(r.right)
        if val_left == -1:
            return -1
        elif val_right == -1:
            return -1
        if abs(val_left-val_right) >= 2:
            return -1
        return max(val_left+1, val_right+1)
        