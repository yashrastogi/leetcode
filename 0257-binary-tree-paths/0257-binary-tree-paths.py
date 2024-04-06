# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return
        paths = []
        tempString = f"{root.val}"

        def backtrack(node):
            nonlocal tempString
            if node.left:
                t = f"->{node.left.val}"
                tempString += t
                backtrack(node.left)
                tempString = tempString[:-len(t)]
            if node.right:
                t = f"->{node.right.val}"
                tempString += t
                backtrack(node.right)
                tempString = tempString[:-len(t)]
            if not node.right and not node.left:
                paths.append(tempString)
        
        backtrack(root)
        return paths