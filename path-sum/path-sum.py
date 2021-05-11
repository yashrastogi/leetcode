# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, sum=0):
            if not node:
                return
            if not node.left and not node.right and sum + node.val == targetSum:
                return True
            return dfs(node.left, sum+node.val) or dfs(node.right, sum+node.val)
        return dfs(root)