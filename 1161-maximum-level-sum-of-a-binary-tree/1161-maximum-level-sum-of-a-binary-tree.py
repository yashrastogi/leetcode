class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dict_depth_sums = defaultdict(int)
        q = [(root, 1)]
        while q:
            curr, depth = q.pop(0)
            dict_depth_sums[depth] += curr.val
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))
        return max(dict_depth_sums, key=lambda depth: (dict_depth_sums[depth], -depth))
