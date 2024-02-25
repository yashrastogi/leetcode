class Solution {
    public int nearestExit(char[][] maze, int[] ent) {
        Set<String> visited = new HashSet<>();
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{ent[0], ent[1], 0});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0], y = curr[1], level = curr[2];
            String key = x + "," + y;

            if (visited.contains(key)) {
                continue;
            }

            visited.add(key);

            if (!isArrayEqual(curr, ent) && (x == 0 || x == maze.length - 1 || y == 0 || y == maze[0].length - 1)) {
                return level;
            }

            int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
            for (int[] dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (0 <= nx && nx < maze.length && 0 <= ny && ny < maze[0].length && maze[nx][ny] == '.') {
                    q.add(new int[]{nx, ny, level + 1});
                }
            }
        }

        return -1;
    }

    private boolean isArrayEqual(int[] arr1, int[] arr2) {
        return arr1[0] == arr2[0] && arr1[1] == arr2[1];
    }
}
