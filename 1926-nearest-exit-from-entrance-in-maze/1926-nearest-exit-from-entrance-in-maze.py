class Solution:
    def nearestExit(self, maze, entrance):
        steps = 0
        rows = len(maze)
        columns = len(maze[0])
        queue = deque([entrance])
        maze[entrance[0]][entrance[1]] = '+'
        options = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            steps += 1
            n = len(queue)
            for _ in range(n):
                current = queue.popleft()
                for option in options:
                    x = current[0] + option[0]
                    y = current[1] + option[1]
                    if x < 0 or x >= rows or y < 0 or y >= columns:
                        continue
                    if maze[x][y] == '+':
                        continue
                    if x == 0 or x == rows - 1 or y == 0 or y == columns - 1:
                        return steps
                    maze[x][y] = '+'
                    queue.append([x, y])
        return -1