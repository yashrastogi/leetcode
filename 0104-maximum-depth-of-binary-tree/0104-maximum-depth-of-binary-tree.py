# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], n=1) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left, n + 1), n, self.maxDepth(root.right, n + 1))
