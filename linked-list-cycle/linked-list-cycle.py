# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ll_set = set()
        while head:
            if head in ll_set:
                return True
            ll_set.add(head)
            head = head.next
        return False