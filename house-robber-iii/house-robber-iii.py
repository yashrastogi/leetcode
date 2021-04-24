# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}
        def rec(node, skipLevel):
            if not node:
                return 0
            if node in memo:
                if skipLevel in memo[node]:
                    return memo[node][skipLevel]
            sum = rec(node.left, not skipLevel) + rec(node.right, not skipLevel)
            sum2 = rec(node.left, skipLevel) + rec(node.right, skipLevel)
            if not skipLevel:
                sum += node.val
            # print(memo)
            memo[node] = memo.setdefault(node, {})
            memo[node].update({skipLevel: max(sum, sum2)})
            return memo[node][skipLevel]
            
        case1 = rec(root, False)
        case2 = rec(root, True)
        print(case1, case2)
        return max(case1, case2)
        