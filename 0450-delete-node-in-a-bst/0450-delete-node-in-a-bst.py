class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root: return list()
            ret = dfs(root.left)
            ret.append(root.val)
            ret.extend(dfs(root.right))
            return ret
        def dfs2(root, parent):
            if not root: return (None, None)
            if root.val == key: return (root, parent)
            return dfs2(root.left, root) or dfs2(root.right, root)
        
        del_node, del_node_parent = dfs2(root, None)
        if not del_node: return root
        arr = dfs(del_node)
        arr.remove(key)
        if len(arr) == 0: return None
        del_node.val = arr[0]
        del_node.left = None
        del_node.right = self.createBST(arr, 1, len(arr) - 1)
        return root

    def createBST(self, arr, ibegin, iend):
        if ibegin == iend:
            return TreeNode(arr[ibegin])
        elif ibegin > iend:
            return None
        mid = (ibegin + iend) // 2
        node = TreeNode(arr[mid])
        node.left = self.createBST(arr, ibegin, mid - 1)
        node.right = self.createBST(arr, mid + 1, iend)
        return node