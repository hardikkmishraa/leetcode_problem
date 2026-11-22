
class Solution:
    def solve(self, node):
        if node is None:
            return 0

        leftsum = self.solve(node.left)
        if leftsum < 0:
            leftsum = 0

        rightsum = self.solve(node.right)
        if rightsum < 0:
            rightsum = 0

        self.maxi = max(self.maxi, leftsum + node.val + rightsum)

        return node.val + max(leftsum, rightsum)

    def maxPathSum(self, root):
        self.maxi = float('-inf')
        self.solve(root)
        return self.maxi
