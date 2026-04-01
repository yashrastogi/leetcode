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
        visited = set()
        while q:
            depth, (i, j) = q.pop(0)
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or (i, j) in visited
            ):
                continue
            if grid[i][j] == 1 and (i, j) not in island_1:
                return depth - 1
            visited.add((i, j))
            q.append((depth + 1, (i + 1, j)))
            q.append((depth + 1, (i, j + 1)))
            q.append((depth + 1, (i - 1, j)))
            q.append((depth + 1, (i, j - 1)))

        return -1
