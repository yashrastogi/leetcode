# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(node, mini=float('-inf'), maxi=float('inf')):
            if not node:
                return True
            # print(node.val, mini, maxi)
            if node.val <= mini or node.val >= maxi:
                return False
            left_min = mini
            left_max = min(maxi, node.val)
            right_min = max(node.val, mini)
            right_max = maxi
            return isValid(node.left, left_min, left_max) and isValid(node.right, right_min, right_max)
        
        return isValid(root)