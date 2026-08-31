# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        val_left = self.maxDepth(root.left)
        val_right = self.maxDepth(root.right)

        return max(val_left+1, val_right+1)