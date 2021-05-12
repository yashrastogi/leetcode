# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bst(lo, hi):
            if lo > hi:
                return
            mid = int((hi + lo) / 2)
            node = TreeNode(nums[mid])
            node.left = bst(lo, mid-1)
            node.right = bst(mid+1, hi)
            return node
        return bst(0, len(nums)-1)