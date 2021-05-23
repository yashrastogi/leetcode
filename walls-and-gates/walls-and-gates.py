class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        WALL, GATE, ROOM = -1, 0, 2147483647
        queue = []
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == GATE:
                    queue.append((i, j, 0))
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        while queue:
            i, j, depth = queue.pop(0)
            if rooms[i][j] == ROOM:
                rooms[i][j] = depth
            for d in directions:
                ix, jx, depthx = i+d[0], j+d[1], depth+1
                if ix>=0 and jx>=0 \
                and ix<len(rooms) and jx<len(rooms[0]) \
                and rooms[ix][jx] == ROOM \
                and (ix, jx) not in visited:
                    visited.add((ix, jx))
                    queue.append((ix, jx, depthx))
        