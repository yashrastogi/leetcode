class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        findMin = lambda node: findMin(node.left) if node.left else node

        def deleteHelper(node, key):
            if not node:
                return
            if key > node.val:
                node.right = deleteHelper(node.right, key)
            elif key < node.val:
                node.left = deleteHelper(node.left, key)
            else: # elif this is the node to delete
                if not node.left: # one child
                    return node.right
                elif not node.right:
                    return node.left
                else: # two children
                    successor = findMin(node.right)
                    node.val = successor.val
                    node.right = deleteHelper(node.right, successor.val)
            return node
        
        return deleteHelper(root, key)
                    

