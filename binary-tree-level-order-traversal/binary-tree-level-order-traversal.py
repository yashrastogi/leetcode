# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rec(node, ret, depth):
    if not node:
        return
    if depth > len(ret)-1:
        ret.append([])
    ret[depth] += [node.val]
    if node.left:
        rec(node.left, ret, depth+1)
    if node.right:
        rec(node.right, ret, depth+1)
    
    
    
    
    

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = [[root.val]]
        rec(root.left, ret, 1)
        rec(root.right, ret, 1)
        return ret