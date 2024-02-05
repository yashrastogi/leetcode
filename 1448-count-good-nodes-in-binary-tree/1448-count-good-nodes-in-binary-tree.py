# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val=root.val):
            if not root:
                return 0
            return (
                int(root.val >= max_val)
                + dfs(root.left, max(max_val, root.val))
                + dfs(root.right, max(max_val, root.val))
            )

        return dfs(root)
