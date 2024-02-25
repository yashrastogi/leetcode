class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append(((x, y), 0))
                    visited.add((x, y))
                elif grid[x][y] == 0:
                    visited.add((x, y))
        max_level = 0
        while q:
            curr, level = q.popleft()
            max_level = max(level, max_level)
            visited.add(curr)
            if len(visited) == len(grid) * len(grid[0]):
                break
            for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                cd = (curr[0] + x, curr[1] + y)
                if (
                    0 <= cd[0] < len(grid)
                    and 0 <= cd[1] < len(grid[0])
                    and cd not in visited
                ):
                    q.append(((cd, level + 1)))
        if len(visited) != len(grid) * len(grid[0]):
            return -1
        return max_level
