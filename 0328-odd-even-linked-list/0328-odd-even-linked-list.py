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
            if odd:
                # print(odd.val, end=' ')
                if odd.next:
                    # print('=> ',odd.next.next)
                    oddPrev = odd
                    odd = odd.next.next
                    oddPrev.next = odd
            if even:
                # print(even.val, end=' ')
                if even.next:
                    # print('=> ',even.next.next)
                    evenPrev = even
                    even = even.next.next
                    evenPrev.next = even
        # print(odd, oddPrev, evenStart)
        if odd:
            odd.next = evenStart
        else:
            oddPrev.next = evenStart
        return head
