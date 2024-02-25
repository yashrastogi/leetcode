class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited, ent = set(), tuple(entrance)
        q = deque([(ent, 0)])
        while q:
            curr, level = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            if curr != ent and (
                curr[0] == 0
                or curr[0] == len(maze) - 1
                or curr[1] == 0
                or curr[1] == len(maze[0]) - 1
            ):
                return level
            for d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                cd = (curr[0] + d[0], curr[1] + d[1])
                if not (
                    cd[0] < 0
                    or cd[1] < 0
                    or cd[0] >= len(maze)
                    or cd[1] >= len(maze[0])
                    or maze[cd[0]][cd[1]] == "+"
                ):
                    q.append((cd, level + 1))
        return -1
