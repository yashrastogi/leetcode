class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        max_sum_depth = 0
        curr_sum = 0
        curr_depth = 0
        q = [(root, 1)]
        while q:
            curr, depth = q.pop(0)
            if depth == curr_depth:
                curr_sum += curr.val
            else:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_sum_depth = curr_depth
                curr_depth = depth
                curr_sum = curr.val
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))
        return max_sum_depth
