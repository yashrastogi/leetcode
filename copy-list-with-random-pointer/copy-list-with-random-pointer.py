"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return
        # create standard copy of list without copying random pointer
        chead = Node(head.val)
        curr, ccurr = head.next, chead
        while curr:
            ccurr.next = Node(curr.val)
            ccurr = ccurr.next
            curr = curr.next
        
        # insert copy node one after original node
        curr, ccurr = head, chead
        while curr:
            temp = curr.next
            temp2 = ccurr.next
            curr.next = ccurr
            ccurr.next = temp
            curr = temp
            ccurr = temp2
        
        # set random pointer from original nodes to copy nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr=curr.next.next
        
        # extract copy nodes from cumulative original + copy list
        ccurr = chead
        while ccurr.next:
            ccurr.next = ccurr.next.next
            ccurr = ccurr.next
        
        return chead