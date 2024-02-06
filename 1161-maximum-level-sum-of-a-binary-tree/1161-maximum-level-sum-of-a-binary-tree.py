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
        max_sum = -float("inf")
        max_sum_depth = 0
        for depth in dict_depth_sums:
            if dict_depth_sums[depth] > max_sum:
                max_sum = dict_depth_sums[depth]
                max_sum_depth = depth
        return max_sum_depth
