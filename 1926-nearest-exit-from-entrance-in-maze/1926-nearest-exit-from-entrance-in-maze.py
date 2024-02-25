class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        ent = tuple(entrance)
        q = deque([(ent, 0)])

        while q:
            curr, level = q.popleft()
            if curr in visited:
                continue

            visited.add(curr)
            x, y = curr

            if curr != ent and (
                x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1
            ):
                return level

            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(maze)
                    and 0 <= ny < len(maze[0])
                    and maze[nx][ny] == "."
                ):
                    q.append(((nx, ny), level + 1))

        return -1

s = Solution()
it = iter(stdin)
f = open('user.out', 'w')

for maze in it:
    ent = loads(next(it))
    f.write(dumps(s.nearestExit(loads(maze), ent)).replace(' ', '') + '\n')

exit()