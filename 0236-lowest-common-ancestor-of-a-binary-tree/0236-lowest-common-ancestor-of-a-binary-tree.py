class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(root, findNode):
            if not root:
                return False
            if root == findNode:
                return True
            return dfs(root.left, findNode) or dfs(root.right, findNode)

        def dfs2(root):
            if not root:
                return None
            a = dfs2(root.left)
            b = dfs2(root.right)
            if a:
                return a
            elif b:
                return b
            elif dfs(root, p) and dfs(root, q):
                return root

        return dfs2(root)