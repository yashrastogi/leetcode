# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 1 and head.next == None:
            return
        if head == None:
            return
        curr, curr2 = head, head
        idx = 1
        incr = False
        while curr.next:
            # print(idx, curr.val)
            if idx == n+1:
                incr = True
            idx+=1
            curr = curr.next
            if incr:
                curr2 = curr2.next
            print(curr2.val, curr.val)
        
        print("--",curr2.val)
        if n == 1:
            print(1)
            curr2.next = None
            return head
        if n == 2 and idx == 2:
            print(2)
            return curr
        if curr2 == head and n == idx:
            print(4)
            head = curr2.next
            return head
        if curr2.next:
            print(3)
            curr2.next = curr2.next.next
            return head
    