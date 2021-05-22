"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        stack = [node]
        mapper = {}
        while stack:
            curr = stack.pop()
            mapper[curr] = Node(curr.val)
            for nbr in curr.neighbors:
                if nbr and nbr not in mapper:
                    stack.append(nbr)
                    mapper[nbr] = None
        
        stack = [node]
        for orig_node in mapper:
            for orig_nbr in orig_node.neighbors:
                mapper[orig_node].neighbors += [mapper[orig_nbr]]
        
        return mapper[node]