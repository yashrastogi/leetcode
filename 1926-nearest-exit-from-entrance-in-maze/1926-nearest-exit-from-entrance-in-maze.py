class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ent = tuple(entrance)
        visited = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q = [(ent, 0)]
        while q:
            curr = q[0][0]
            level = q[0][1]
            q.pop(0)
            if (
                curr[0] < 0
                or curr[1] < 0
                or curr[0] >= len(maze)
                or curr[1] >= len(maze[0])
                or maze[curr[0]][curr[1]] == "+"
                or curr in visited
            ):
                continue
            visited.add(curr)
            if curr != ent and (
                curr[0] == 0
                or curr[0] == len(maze) - 1
                or curr[1] == 0
                or curr[1] == len(maze[0]) - 1
            ):
                return level
            for d in directions:
                cd = (curr[0] + d[0], curr[1] + d[1])
                q.append((cd, level + 1))
        return -1
