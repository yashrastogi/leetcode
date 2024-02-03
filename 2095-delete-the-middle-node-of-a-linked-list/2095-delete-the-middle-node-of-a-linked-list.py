# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        faster = curr
        prev = None
        while faster and faster.next:
            faster = faster.next.next
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
            return head
        else:
            return None
