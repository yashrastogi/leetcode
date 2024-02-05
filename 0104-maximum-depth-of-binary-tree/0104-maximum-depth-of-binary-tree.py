# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, n = 1):
            if not root: return 0
            n1 = dfs(root.left, n + 1)
            n2 = dfs(root.right, n + 1)
            return max(n1, n, n2)
        return dfs(root)