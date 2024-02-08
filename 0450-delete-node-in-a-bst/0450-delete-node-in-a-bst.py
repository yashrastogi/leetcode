class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            if not root.left: return root
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
            min_node = findMin(key_node[0].right)
            key_node[0].val = min_node.val
            print(min_node)
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
