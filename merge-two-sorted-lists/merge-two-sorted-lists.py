# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        
        l1n = l1
        l2n = l2
        retn_head = ListNode(-101)
        retn = retn_head
        while l1n and l2n:
            if l1n.val <= l2n.val:
                # print(l1n.val)
                if retn.val == -101:
                    retn.val = l1n.val
                else:
                    retn.next = ListNode(l1n.val)
                    retn = retn.next
                l1n = l1n.next
            else:
                # print(l2n.val)
                if retn.val == -101:
                    retn.val = l2n.val
                else:
                    retn.next = ListNode(l2n.val)
                    retn = retn.next
                l2n = l2n.next
        while l1n:
            if retn.val == -101:
                retn.val = l1n.val
            else:
                retn.next = ListNode(l1n.val)
                retn = retn.next
            l1n = l1n.next
        while l2n:
            if retn.val == -101:
                retn.val = l2n.val
            else:
                retn.next = ListNode(l2n.val)
                retn = retn.next
            l2n = l2n.next
            
        return retn_head
                
            