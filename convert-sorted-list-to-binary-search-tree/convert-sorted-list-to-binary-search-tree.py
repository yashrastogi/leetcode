# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def rec(lo, hi):
            if lo > hi: return
            nonlocal sorted_list
            mid = int((lo+hi)/2)
            node = TreeNode(sorted_list[mid])
            node.left = rec(lo, mid-1)
            node.right = rec(mid+1, hi)
            return node
        
        sorted_list = []
        while head:
            sorted_list.append(head.val)
            head = head.next

        return rec(0, len(sorted_list)-1)