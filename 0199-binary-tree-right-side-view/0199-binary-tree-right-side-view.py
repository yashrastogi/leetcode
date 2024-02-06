# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        q = [(root, 0)]
        prevDepth = 0
        prevElem = root
        while q:
            curr, depth = q.pop(0)
            if depth != prevDepth:
                prevDepth = depth
                ret.append(prevElem.val)
            prevElem = curr 
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))
        ret.append(prevElem.val)
        return ret