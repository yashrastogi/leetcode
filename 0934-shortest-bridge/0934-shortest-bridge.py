from pprint import pprint


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island_1 = set()

        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] == 0
                or (i, j) in island_1
            ):
                return
            island_1.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not found:
                    dfs(i, j)
                    found = True

        q = [(0, p) for p in island_1]
        visited = island_1.copy()
        while q:
            d, (i, j) = q.pop(0)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    0 <= x < len(grid)
                    and 0 <= y < len(grid[0])
                    and (x, y) not in visited
                ):
                    if grid[x][y] == 1:
                        return d  # shortest bridge found

                    visited.add((x, y))
                    q.append((d + 1, (x, y)))

        return -1
