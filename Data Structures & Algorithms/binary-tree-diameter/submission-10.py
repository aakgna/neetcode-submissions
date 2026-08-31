# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.track = []  
        self.helper(root)
        return max(self.track)
    def helper(self, root):
        if root == None:
            return 0
        val_left = self.helper(root.left)
        val_right = self.helper(root.right)
        if root.left != None:
            val_left += 1
        if root.right != None:
            val_right += 1
        self.track.append(val_left + val_right)
        return max(val_left, val_right)
