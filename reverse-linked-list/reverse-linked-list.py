# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        count = 0
        prevNode = None
        while curr != None:
            if count == 0:
                # last node
                newNode = ListNode(curr.val)
            else:
                # not last node
                newNode = ListNode(curr.val, prevNode)
            prevNode = newNode
            curr = curr.next
            count += 1
        return prevNode