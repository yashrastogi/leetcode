function nearestExit(maze, entrance) {
        const visited = new Set();
        const ent = entrance;
        const q = [ [ent, 0] ];

        while (q.length > 0) {
            const [curr, level] = q.shift();

            if (visited.has(curr.toString())) {
                continue;
            }

            visited.add(curr.toString());
            const [x, y] = curr;

            if (
                curr.toString() !== ent.toString() &&
                (x === 0 || x === maze.length - 1 || y === 0 || y === maze[0].length - 1)
            ) {
                return level;
            }

            const directions = [[0, 1], [1, 0], [-1, 0], [0, -1]];
            for (const [dx, dy] of directions) {
                const nx = x + dx;
                const ny = y + dy;
                if (
                    nx >= 0 && nx < maze.length &&
                    ny >= 0 && ny < maze[0].length &&
                    maze[nx][ny] === "."
                ) {
                    q.push([[nx, ny], level + 1]);
                }
            }
        }

        return -1;
    }