class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_length = 0

        def dfs(node: TreeNode, goLeft: bool, length: int) -> None:
            self.max_length = max(self.max_length, length)

            if goLeft:
                if node.left:
                    dfs(node.left, False, length + 1)
                if node.right:
                    dfs(node.right, True, 1)
            else:
                if node.right:
                    dfs(node.right, True, length + 1)
                if node.left:
                    dfs(node.left, False, 1)

        if not root:
            return 0

        dfs(root, True, 0)
        dfs(root, False, 0)

        return self.max_length
