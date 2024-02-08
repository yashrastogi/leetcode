class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root, parent):
            if not root.left: return (root, parent)
            return findMin(root.left)

        def findKey(root, parent=None, isLeft=False):
            if not root:
                return
            if root.val == key:
                return (root, parent, isLeft)
            elif key > root.val:
                return findKey(root.right, root, False)
            else:
                return findKey(root.left, root, True)

        key_node = findKey(root)
        if not key_node:
            return root  # not found
        if not key_node[0].left and not key_node[0].right:  # no children
            if key_node[2]:
                key_node[1].left = None
            else:
                key_node[1].right = None
        if not key_node[0].left:  # only one child
            if key_node[2]:
                key_node[1].left = key_node[0].right
            else:
                key_node[1].right = key_node[0].right
        if not key_node[0].right:  # only one child
            if key_node[2]:
                key_node[1].left = key_node[0].left
            else:
                key_node[1].right = key_node[0].left
        if key_node[0].left and key_node[0].right: # two children
            min_node = findMin(key_node[0].right, key_node[0])
            key_node[0].val = min_node[0].val
            min_node[1].right = None
        return root