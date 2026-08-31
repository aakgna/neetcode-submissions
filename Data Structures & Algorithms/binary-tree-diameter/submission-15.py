# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root)
        return self.res
    def helper(self, root):
        if root == None:
            return 0
        val_left = self.helper(root.left)
        val_right = self.helper(root.right)
        if root.left != None:
            val_left += 1
        if root.right != None:
            val_right += 1
        if val_left + val_right > self.res:
            self.res = val_left + val_right
        return max(val_left, val_right)
