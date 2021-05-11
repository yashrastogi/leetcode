# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = None
        while curr:
            # print(curr.val)
            if curr.val == val:
                if curr == head:
                    head = curr.next
                else:
                    temp = curr
                    while temp and temp.val == val:
                        temp=temp.next
                    prev.next = temp
            prev = curr
            curr = curr.next
        return head