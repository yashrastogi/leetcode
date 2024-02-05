class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, csum):
            ret = int(csum == targetSum)
            left = 0
            right = 0
            if root.left:
                left = dfs(root.left, csum + root.left.val)
            if root.right:
                right = dfs(root.right, csum + root.right.val)
            return left + right + ret

        if not root:
            return 0
        return (
            dfs(root, root.val)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
