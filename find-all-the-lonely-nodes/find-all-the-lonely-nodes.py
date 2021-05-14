# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        stack = [(root, root)]
        ret = []
        while stack:
            curr, prev = stack.pop()
            if curr != root:
                if not prev.left or not prev.right:
                    ret.append(curr.val)
            if curr.left:
                stack.append((curr.left, curr))
            if curr.right:
                stack.append((curr.right, curr))
        return ret