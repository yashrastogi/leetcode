# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def rec(root):
            if not root:
                return
            cp = TreeNode(root.val)
            cp.left = rec(root.right)
            cp.right = rec(root.left)
            return cp
        return rec(root)
        
        