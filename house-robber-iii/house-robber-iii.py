# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rec(node):
    if not node:
        return [0,0]
    l = rec(node.left)
    r = rec(node.right)
    return [node.val + l[1] + r[1], max(l) + max(r)]

class Solution:
    def rob(self, root: TreeNode) -> int:    
        return max(rec(root))
        