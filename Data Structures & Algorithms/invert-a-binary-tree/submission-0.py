# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = list()
        curr = root
        queue.append(curr)
        while len(queue) > 0:
            temp = queue.pop()
            if temp == None:
                continue
            temp_l = temp.left
            temp.left = temp.right
            temp.right = temp_l
            queue.append(temp.right)
            queue.append(temp.left)
        return root