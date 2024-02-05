class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        fast = head
        prev_curr = None
        while fast and fast.next:
            fast = fast.next.next
            prev_curr = curr
            curr = curr.next
        prev_curr.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        maxTwinSum = 0
        while head:
            maxTwinSum = max(maxTwinSum, head.val + prev.val)
            head = head.next
            prev = prev.next
        return maxTwinSum
