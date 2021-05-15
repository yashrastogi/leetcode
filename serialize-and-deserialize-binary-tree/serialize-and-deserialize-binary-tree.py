class Codec:
    def serialize(self, root):
        def _rec(node):
            nonlocal strng
            if not node: return
            if not node.left:
                strng += ["null"]
            if node.left:
                strng += [str(node.left.val)]
            if not node.right:
                strng += ["null"]
            if node.right:
                strng += [str(node.right.val)]
            _rec(node.left)
            _rec(node.right)
        
        if root == None: return ""
        strng = [str(root.val)]
        _rec(root)
        return ",".join(strng)
        
    def deserialize(self, ret):
        if ret == '': return None
        ret = ret.split(',')
        root = TreeNode(ret.pop(0))
        def _rec(node):
            nonlocal ret
            if not node: return
            c = ret.pop(0)
            if ret and c != 'null':
                node.left = TreeNode(c)
            c = ret.pop(0)
            if ret and c != 'null':
                node.right = TreeNode(c)
            _rec(node.left)
            _rec(node.right)
        _rec(root)
        return root