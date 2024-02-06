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

        def dfs2(root, depth=0):
            if not root:
                return None
            a = dfs2(root.left, depth + 1)
            b = dfs2(root.right, depth + 1)
            if a and b:
                if a[1] > b[1]:
                    return a
                else:
                    return b
            elif a:
                return a
            elif b:
                return b
            elif dfs(root, p) and dfs(root, q):
                return (root, depth)

        return dfs2(root)[0]
