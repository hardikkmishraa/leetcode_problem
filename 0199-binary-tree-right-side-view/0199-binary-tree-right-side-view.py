class Solution:
    def dfs(self, node, depth, result):
        if not node:
            return

        # If this depth is being visited for the first time, add node
        if depth == len(result):
            result.append(node.val)

        # Visit right child first, then left child
        self.dfs(node.right, depth + 1, result)
        self.dfs(node.left, depth + 1, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, 0, result)
        return result