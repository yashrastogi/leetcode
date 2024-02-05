class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, csum):
            ret = int(csum == targetSum)
            if root.left:
                ret += dfs(root.left, csum + root.left.val)
            if root.right:
                ret += dfs(root.right, csum + root.right.val)
            return ret

        if not root:
            return 0
        return (
            dfs(root, root.val)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
