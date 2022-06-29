# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lookup = {}
        list_len = 0
        curr = head
        while curr:
            lookup[list_len] = curr
            list_len += 1
            curr = curr.next
        
        lo, hi = 0, list_len-1
        prev_node_next = head.next
        while lo < hi:
            temp = lookup[lo].next
            lookup[lo].next = lookup[hi]
            lookup[hi].next = temp
            lo += 1
            hi -= 1
        if list_len % 2 != 0:
            lookup[hi].next = None
        else:
            lookup[hi+1].next = None
          