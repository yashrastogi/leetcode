class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        evenStart = even
        oddPrev = None
        evenPrev = None
        while odd and even:
            if odd and odd.next:
                oddPrev = odd
                odd = odd.next.next
                oddPrev.next = odd
            if even and even.next:
                evenPrev = even
                even = even.next.next
                evenPrev.next = even
        if odd:
            odd.next = evenStart
        else:
            oddPrev.next = evenStart
        return head
