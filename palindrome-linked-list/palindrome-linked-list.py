# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num_str = ''
        while head:
            num_str += str(head.val)
            head = head.next
        return int(num_str) == int(num_str[::-1])