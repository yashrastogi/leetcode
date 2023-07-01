# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        ret = ''
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr:
                ret += str(curr.val) + ' '
            else:
                ret += 'x '
                continue
            q.append(curr.left)
            q.append(curr.right)
        return ret

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data_split = data.split(' ')[:-1]
        print(data_split)
        if not len(data_split): return None
        root = TreeNode(data_split[0])
        q = deque([root])
        i = 1
        while q:
            curr = q.popleft()
            if data_split[i] == 'x':
                curr.left = None
            else:
                curr.left = TreeNode(data_split[i])
                q.append(curr.left)
            i += 1
            if data_split[i] == 'x':
                curr.right = None
            else:
                curr.right = TreeNode(data_split[i])
                q.append(curr.right)
            i += 1
        return root


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans