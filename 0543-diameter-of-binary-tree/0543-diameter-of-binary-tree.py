# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter=0
    def height(self,root):
        if not root:
            return 0
        leftheight=self.height(root.left)
        rightheight=self.height(root.right)

        self.diameter=max(self.diameter,leftheight+rightheight)
        return 1+max(leftheight,rightheight)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.height(root)
        return self.diameter
        