# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        heap = []
        for head in lists:
            curr = head
            while curr:
                heappush(heap, curr.val)
                curr = curr.next
            head = None
        if len(heap) == 0:
            return None
        head = ListNode(heappop(heap))
        curr = head
        for _ in range(1, len(heap)+1):
            node = ListNode(heappop(heap))
            curr.next = node
            curr = node
        return head