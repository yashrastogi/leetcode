# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        par = {}
        def dfs(root, parent=None):
            par[root] = parent
            l, r = root.left, root.right
            if l: dfs(l, root)
            if r: dfs(r, root)
        dfs(root)
        
        ret = []
        q = [ (target, 0) ]
        visited = set([target])
        while q:
            curr, depth = q.pop(0)
            if depth == k:
                ret += [curr.val]
            nbrs = [curr.left, curr.right, par[curr]]
            for nbr in nbrs:
                if nbr and nbr not in visited:
                    visited.add(nbr)
                    q += [(nbr, depth + 1)]
            
        return ret