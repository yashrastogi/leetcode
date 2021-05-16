class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def appendQ(tup):
            nonlocal count,i,j
            if (tup[0], tup[1]) not in visited:
                visited[(tup[0], tup[1])] = visited[(i,j)] + 1
                queue.append((tup[0],tup[1]))
        
        visited = {(0,0): 0}
        
        queue = [(0,0)]
        count = 0
        while queue:
            i, j = queue.pop(0)
            if (i, j) == (x, y):
                return visited[(i,j)]
            appendQ((i+1, j-2))
            appendQ((i+2, j-1))
            appendQ((i+2, j+1))
            appendQ((i+1, j+2))
            appendQ((i-1, j-2))
            appendQ((i-2, j-1))
            appendQ((i-1, j+2))
            appendQ((i-2, j+1))
        
        print(visited)
        return 0