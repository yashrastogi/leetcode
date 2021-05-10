# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        order_nodes = []
        curr = head
        while curr:
            order_nodes.append(curr)
            curr = curr.getNext()
        for el in reversed(order_nodes):
            el.printValue()