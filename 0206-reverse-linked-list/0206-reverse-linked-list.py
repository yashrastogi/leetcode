# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ptr1 = head  # 1
        ptr2 = head.next  # 2
        prevPtr1 = None
        while ptr2:
            temp = ptr2.next  # 3 ; 4
            ptr2.next = ptr1  # 2 -> 1 ; 3 -> 2 ;
            ptr1.next = prevPtr1  # 1 -> None ; 2 -> 1
            prevPtr1 = ptr1
            ptr1 = ptr2  # 2
            ptr2 = temp  # 3
        return ptr1
