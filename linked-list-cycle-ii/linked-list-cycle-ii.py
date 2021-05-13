# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        first_meet = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                first_meet = fast
                break
        
        slow = head
        while slow and first_meet:
            if slow == first_meet:
                return slow
            first_meet = first_meet.next
            slow = slow.next