class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROOM, GATE, WALL = 2147483647, 0, -1
        
        queue = []
        
        def bfs():
            nonlocal queue
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while queue:
                i, j = queue.pop(0)
                for d in directions:
                    ix, jx = i+d[0], j+d[1]
                    if ix >= 0 and jx >= 0 \
                    and ix < len(rooms) and jx < len(rooms[0]) \
                    and rooms[ix][jx] == ROOM:
                        rooms[ix][jx] = rooms[i][j]+1
                        queue.append((ix, jx))
        
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y] == GATE:
                    queue.append((x, y))
        
        bfs()        